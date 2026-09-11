# Sangam — Deployment Guide

## Quick Start (Local Development)

### Prerequisites
- Python 3.11+
- Docker & Docker Compose (for database)
- [Gemini API key](https://aistudio.google.com/apikey) (free tier is sufficient)

### Option A: Docker Compose (Recommended)

Starts both the PostgreSQL database and the backend API:

```bash
# 1. Clone and enter the repo
git clone https://github.com/your-org/sangam.git
cd sangam

# 2. Create environment file
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY

# 3. Start everything (first run with demo data)
SEED_DB=true docker compose up --build

# 4. Access the API
#    API:     http://localhost:8000
#    Swagger: http://localhost:8000/docs
#    Health:  http://localhost:8000/health
```

Subsequent runs (data persists in the `pgdata` volume):
```bash
docker compose up --build
```

To reset the database:
```bash
docker compose down -v   # removes the pgdata volume
SEED_DB=true docker compose up --build
```

### Option B: Local Python + Docker DB

Use Docker only for the database, run the backend natively:

```bash
# 1. Start only the database
docker compose up db -d

# 2. Set up the backend
cd backend
cp .env.example .env
# Edit .env — DATABASE_URL should point to localhost:5432

# 3. Install dependencies
pip install -r requirements.txt

# 4. Initialize the database
python -m app.utils.db_init

# 5. (Optional) Seed demo data
python -m app.utils.db_seed

# 6. Start the API server
uvicorn app.main:app --reload --port 8000
```

---

## Running Tests

```bash
cd backend
python -m pytest tests/ -v --tb=short
```

Tests mock the database, so no PostgreSQL is needed.

---

## Production Deployment

### Backend + Database → Railway

Both the API and its Postgres/PostGIS/pgvector database run on
[Railway](https://railway.com/), as two services in one project.

**1. Database service** (`db/Dockerfile`):
1. In the Railway dashboard: **New → Empty Service**, then set its source
   to this repo with **Root Directory** = `db` (Railway builds
   `db/Dockerfile` — a `pgvector/pgvector` base with PostGIS added via
   apt, chosen over the `supabase/postgres` image because it needs no
   bootstrap-role workaround to run `CREATE EXTENSION` on a fresh volume).
2. Attach a **Volume** mounted at `/var/lib/postgresql/data` so data
   survives redeploys.
3. Set variables: `POSTGRES_DB=sangam`, `POSTGRES_USER=postgres`,
   `POSTGRES_PASSWORD=<generate a strong value>`.
4. Note the service's private/internal `DATABASE_URL` — Railway exposes it
   as a reference variable other services in the same project can consume
   directly (see below), no copy-pasting a connection string by hand.

**2. Backend service** (`backend/Dockerfile`):
1. **New → GitHub Repo** (or `railway up` from the `backend/` directory),
   with **Root Directory** = `backend`.
2. Railway assigns the container's listen port dynamically via `$PORT`;
   the Dockerfile's `CMD` already reads it (`--port ${PORT:-8000}`), so no
   start-command override is needed.
3. Add environment variables:
   | Variable | Value |
   |----------|-------|
   | `DATABASE_URL` | `${{<db-service-name>.DATABASE_URL}}` — a Railway reference variable pointing at the Postgres service above |
   | `GEMINI_API_KEY` | Your Gemini API key |
   | `ACTIVE_COUNTRY_PACK` | `india_karnataka` |
   | `PACKS_DIR` | `packs` |
   | `ENV` | `production` |
   | `ADMIN_TOKEN` | A strong random value (gates `/api/v1/admin/*`) |
   | `REPORTER_HASH_PEPPER` | `python -c "import secrets; print(secrets.token_hex(32))"` |
4. Railway builds and deploys on every push to the linked branch. The
   Dockerfile's `HEALTHCHECK` and the app's own `/health` endpoint back
   Railway's deploy health checks.
5. Once live, run the one-time setup commands against the deployed service
   with `railway run`:
   ```bash
   railway run --service backend python -m app.utils.db_init
   railway run --service backend python -m app.utils.db_seed        # demo data
   railway run --service backend python -m app.utils.load_real_data # real Karnataka data
   ```

### Frontend → Vercel

1. Connect the repo to [Vercel](https://vercel.com/)
2. Set **Root directory**: `frontend`
3. Set the backend API URL (the Railway backend service's public domain)
   as an environment variable

---

## Environment Variables Reference

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `DATABASE_URL` | Yes | `postgresql://postgres:postgres@localhost:5432/sangam` | PostgreSQL connection string |
| `ASYNC_DATABASE_URL` | No | Auto-derived from `DATABASE_URL` | Async driver URL (asyncpg) |
| `GEMINI_API_KEY` | Yes* | `None` | Google AI Studio API key |
| `GEMINI_MODEL` | No | `gemini-2.5-flash` | Text generation model |
| `GEMINI_EMBEDDING_MODEL` | No | `text-embedding-004` | Embedding model (768d) |
| `ACTIVE_COUNTRY_PACK` | No | `india_karnataka` | Active pack name |
| `PACKS_DIR` | No | `packs` | Path to pack configs directory |
| `ENV` | No | `development` | `development` or `production` |
| `SEED_DB` | No | `false` | Set `true` for Docker auto-seed |
| `LOAD_REAL_DATA` | No | `false` | Set `true` to import real Karnataka data on start |
| `ADMIN_TOKEN` | Production only | `None` | Shared-secret header gating `/api/v1/admin/*` |
| `REPORTER_HASH_PEPPER` | Production only | Fixed dev fallback | HMAC pepper for hashing citizen channel IDs |

\* The app starts without `GEMINI_API_KEY` but AI features return fallback values.

---

## Architecture

```
┌──────────────┐     ┌──────────────────┐     ┌──────────────────┐
│   Frontend   │────▶│  Backend (API)   │────▶│   PostgreSQL     │
│  React/Vite  │     │  FastAPI/Python  │     │  PostGIS+pgvector│
│   Vercel     │     │    Railway       │     │    Railway       │
└──────────────┘     └───────┬──────────┘     └──────────────────┘
                             │
                     ┌───────▼──────────┐
                     │  Gemini API      │
                     │  (AI Studio)     │
                     └──────────────────┘
```
