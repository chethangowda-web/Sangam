# ─────────────────────────────────────────────────────────────────────────────
# Sangam — Postgres + PostGIS + pgvector
# ─────────────────────────────────────────────────────────────────────────────
# Deployed as its own Railway service (Docker image, not the built-in
# "Add Database" Postgres template, which does not ship PostGIS or pgvector).
# Built on the official PostGIS image; pgvector is added via the same PGDG
# apt repo that image already relies on for the PostGIS packages themselves,
# so no extra repo configuration is needed.
# ─────────────────────────────────────────────────────────────────────────────
FROM pgvector/pgvector:pg16-bookworm

RUN apt-get update \
    && apt-get install -y --no-install-recommends postgresql-16-postgis-3 \
    && rm -rf /var/lib/apt/lists/*
