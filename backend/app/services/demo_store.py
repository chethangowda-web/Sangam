"""
Demo Data Store for Local Development and Graceful Database Fallback.

Provides realistic, pre-computed demonstration data for Karnataka (Bangalore, Chitradurga)
when PostgreSQL is offline, enabling immediate out-of-the-box frontend rendering without
requiring an external database daemon.
"""

from typing import Optional, List, Dict, Any
from datetime import datetime

class DemoStore:
    def __init__(self):
        self._regions = [
            {"id": 1, "country_code": "IND", "name": "Karnataka", "level": "state", "parent_id": None, "population": 61095297},
            {"id": 2, "country_code": "IND", "name": "Bengaluru Urban", "level": "district", "parent_id": 1, "population": 9621551},
            {"id": 3, "country_code": "IND", "name": "Indiranagar Ward", "level": "ward", "parent_id": 2, "population": 38000},
            {"id": 4, "country_code": "IND", "name": "Koramangala Ward", "level": "ward", "parent_id": 2, "population": 45000},
            {"id": 5, "country_code": "IND", "name": "HSR Layout Ward", "level": "ward", "parent_id": 2, "population": 52000},
            {"id": 6, "country_code": "IND", "name": "Chitradurga", "level": "district", "parent_id": 1, "population": 1659456},
            {"id": 7, "country_code": "IND", "name": "Hiriyur", "level": "subdistrict", "parent_id": 6, "population": 290000},
        ]

        self._clusters = [
            {
                "id": 1,
                "title": "Severe Drinking Water Shortage & Pipe Ruptures",
                "sector": "water",
                "region_id": 3,
                "region_name": "Indiranagar Ward",
                "report_count": 8,
                "created_at": "2026-08-20T10:00:00",
                "centroid": "POINT(77.6405 12.9792)",
                "is_approximate_location": False,
                "priority": {
                    "id": 1,
                    "score": 92.4,
                    "verdict": "UNSERVED_GAP"
                }
            },
            {
                "id": 2,
                "title": "Arterial Road Potholes & Stalled Asphalt Repair",
                "sector": "roads",
                "region_id": 4,
                "region_name": "Koramangala Ward",
                "report_count": 10,
                "created_at": "2026-08-21T11:30:00",
                "centroid": "POINT(77.6234 12.9351)",
                "is_approximate_location": False,
                "priority": {
                    "id": 2,
                    "score": 88.1,
                    "verdict": "STALLED_ALLOCATION"
                }
            },
            {
                "id": 3,
                "title": "Uncleared Solid Waste Heap & Disease Vector Risk",
                "sector": "sanitation",
                "region_id": 5,
                "region_name": "HSR Layout Ward",
                "report_count": 6,
                "created_at": "2026-08-22T09:15:00",
                "centroid": "POINT(77.6385 12.9056)",
                "is_approximate_location": False,
                "priority": {
                    "id": 3,
                    "score": 74.5,
                    "verdict": "DELIVERY_GAP"
                }
            },
            {
                "id": 4,
                "title": "Primary Health Centre Critical Medicine Deficit",
                "sector": "health",
                "region_id": 7,
                "region_name": "Hiriyur",
                "report_count": 5,
                "created_at": "2026-08-23T14:45:00",
                "centroid": "POINT(76.6200 13.9450)",
                "is_approximate_location": False,
                "priority": {
                    "id": 4,
                    "score": 68.0,
                    "verdict": "UNDERFUNDED_CRITICAL"
                }
            },
            {
                "id": 5,
                "title": "Frequent Voltage Fluctuation on Feeder Line",
                "sector": "electricity",
                "region_id": 4,
                "region_name": "Koramangala Ward",
                "report_count": 5,
                "created_at": "2026-08-24T16:20:00",
                "centroid": "POINT(77.6280 12.9310)",
                "is_approximate_location": False,
                "priority": {
                    "id": 5,
                    "score": 45.2,
                    "verdict": "WELL_SERVED"
                }
            }
        ]

        self._priorities = [
            {
                "id": 1,
                "cluster_id": 1,
                "title": "Severe Drinking Water Shortage & Pipe Ruptures",
                "sector": "water",
                "score": 92.4,
                "verdict": "UNSERVED_GAP",
                "report_count": 8,
                "region_name": "Indiranagar Ward",
                "details": {"urgency_factor": 4.8, "density": 0.35, "vulnerability": 0.30},
                "list_type": "fund"
            },
            {
                "id": 2,
                "cluster_id": 2,
                "title": "Arterial Road Potholes & Stalled Asphalt Repair",
                "sector": "roads",
                "score": 88.1,
                "verdict": "STALLED_ALLOCATION",
                "report_count": 10,
                "region_name": "Koramangala Ward",
                "details": {"urgency_factor": 4.2, "stalled_amount": 4500000.0},
                "list_type": "audit"
            },
            {
                "id": 3,
                "cluster_id": 3,
                "title": "Uncleared Solid Waste Heap & Disease Vector Risk",
                "sector": "sanitation",
                "score": 74.5,
                "verdict": "DELIVERY_GAP",
                "report_count": 6,
                "region_name": "HSR Layout Ward",
                "details": {"urgency_factor": 3.4},
                "list_type": "fund"
            },
            {
                "id": 4,
                "cluster_id": 4,
                "title": "Primary Health Centre Critical Medicine Deficit",
                "sector": "health",
                "score": 68.0,
                "verdict": "UNDERFUNDED_CRITICAL",
                "report_count": 5,
                "region_name": "Hiriyur",
                "details": {"urgency_factor": 4.5, "vulnerability": 0.62},
                "list_type": "fund"
            },
            {
                "id": 5,
                "cluster_id": 5,
                "title": "Frequent Voltage Fluctuation on Feeder Line",
                "sector": "electricity",
                "score": 45.2,
                "verdict": "WELL_SERVED",
                "report_count": 5,
                "region_name": "Koramangala Ward",
                "details": {"urgency_factor": 2.5},
                "list_type": "fund"
            }
        ]

        self._priority_details = {
            1: {
                "id": 1,
                "score": 92.4,
                "verdict": "UNSERVED_GAP",
                "evidence_bundle": {
                    "report_count": 8,
                    "average_urgency": 4.8,
                    "vulnerability_index": 0.30,
                    "allocated_budget": 0.0,
                    "estimated_cost": 3500000.0,
                    "expenditure_records": [],
                    "citizen_quotes": [
                        "There is no drinking water in Indiranagar for the last 10 days.",
                        "Drinking water pipe leakage has resulted in zero water pressure. No water for our daily chores.",
                        "No municipal water tanker has come in over a week. Buying bottled water for cooking."
                    ]
                },
                "narrative_brief": {
                    "summary": "Severe drinking water deficiency in Indiranagar Ward with 8 recurring citizen reports and 0 sanctioned expenditure.",
                    "why_prioritized": "Identified as an Unserved Gap due to high urgency (4.8/5.0), complete lack of municipal piped supply, and zero allocated capital in the current fiscal budget.",
                    "fiscal_gap_analysis": "The estimated remediation cost is ₹35,00,000. Existing sanctioned expenditure is ₹0, representing a 100% fiscal allocation gap.",
                    "recommended_action": "Sanction emergency pipeline remediation and deploy 3 municipal water tankers daily until mains pressure is restored."
                }
            },
            2: {
                "id": 2,
                "score": 88.1,
                "verdict": "STALLED_ALLOCATION",
                "evidence_bundle": {
                    "report_count": 10,
                    "average_urgency": 4.2,
                    "vulnerability_index": 0.25,
                    "allocated_budget": 4500000.0,
                    "estimated_cost": 4500000.0,
                    "expenditure_records": [
                        {"title": "Pothole Remediation & Asphalt Overlays - Koramangala 80 Feet Rd", "amount": 4500000.0, "status": "stalled"}
                    ],
                    "citizen_quotes": [
                        "There are huge potholes on Koramangala 80 Feet Road. Two-wheeler riders are falling.",
                        "Road repair work has not started in Koramangala. The potholes are still there.",
                        "Contractor abandoned the asphalt work over 3 months ago."
                    ]
                },
                "narrative_brief": {
                    "summary": "Stalled road overlay project on Koramangala 80 Feet Road with ₹45 Lakhs allocated but zero execution on ground.",
                    "why_prioritized": "High citizen demand (10 reports, 4.2 urgency) on an active arterial corridor where public funds were fully sanctioned but contractor execution has halted.",
                    "fiscal_gap_analysis": "₹45,00,000 was allocated in FY25. Status is marked stalled with no contractor milestone updates for >90 days.",
                    "recommended_action": "Issue audit notice to executing agency and invoke contractual penalty clause to resume resurfacing."
                }
            },
            3: {
                "id": 3,
                "score": 74.5,
                "verdict": "DELIVERY_GAP",
                "evidence_bundle": {
                    "report_count": 6,
                    "average_urgency": 3.4,
                    "vulnerability_index": 0.45,
                    "allocated_budget": 2500000.0,
                    "estimated_cost": 2500000.0,
                    "expenditure_records": [
                        {"title": "Borewell Water Treatment & Waste Hub", "amount": 2500000.0, "status": "completed"}
                    ],
                    "citizen_quotes": [
                        "HSR layout sector 3 garbage pile is not cleared. Very bad smell and mosquito breeding.",
                        "Garbage collection truck has skipped Sector 3 for the third time this month."
                    ]
                },
                "narrative_brief": {
                    "summary": "Delivery gap in HSR Layout Sector 3 regarding municipal solid waste collection.",
                    "why_prioritized": "Waste facility marked as completed on records, but citizen reports show recurring lapses in collection routing.",
                    "fiscal_gap_analysis": "Operational routing failure rather than capital expenditure shortfall.",
                    "recommended_action": "Audit ward sanitation contractor route logs and enforce GPS tracking on compactor trucks."
                }
            },
            4: {
                "id": 4,
                "score": 68.0,
                "verdict": "UNDERFUNDED_CRITICAL",
                "evidence_bundle": {
                    "report_count": 5,
                    "average_urgency": 4.5,
                    "vulnerability_index": 0.62,
                    "allocated_budget": 1200000.0,
                    "estimated_cost": 4500000.0,
                    "expenditure_records": [
                        {"title": "PHC Facility Maintenance", "amount": 1200000.0, "status": "in_progress"}
                    ],
                    "citizen_quotes": [
                        "Severe shortage of essential antibiotics and diagnostic reagents at Hiriyur PHC.",
                        "Patients referred 40km away for basic tests."
                    ]
                },
                "narrative_brief": {
                    "summary": "Hiriyur Primary Health Centre requires additional budgetary allocation for essential medicines.",
                    "why_prioritized": "High vulnerability area (0.62) with critical healthcare dependency.",
                    "fiscal_gap_analysis": "Current allocation of ₹12 Lakhs covers building upkeep only; ₹33 Lakh medical equipment gap remains.",
                    "recommended_action": "Allocate supplementary healthcare grant for pharmacy inventory."
                }
            },
            5: {
                "id": 5,
                "score": 45.2,
                "verdict": "WELL_SERVED",
                "evidence_bundle": {
                    "report_count": 5,
                    "average_urgency": 2.5,
                    "vulnerability_index": 0.20,
                    "allocated_budget": 8500000.0,
                    "estimated_cost": 8500000.0,
                    "expenditure_records": [
                        {"title": "BESCOM Substation Feeder Upgrade", "amount": 8500000.0, "status": "completed"}
                    ],
                    "citizen_quotes": [
                        "Occasional evening voltage dips during peak load."
                    ]
                },
                "narrative_brief": {
                    "summary": "Power supply infrastructure is well-maintained with ongoing transformer load balancing.",
                    "why_prioritized": "Low vulnerability and high existing public investment; issue is transient.",
                    "fiscal_gap_analysis": "No additional capital intervention required.",
                    "recommended_action": "Routine maintenance by BESCOM distribution team."
                }
            }
        }

        self._reports = [
            {
                "id": 1,
                "raw_text": "ಇಂದಿರಾನಗರದಲ್ಲಿ ಕಳೆದ ೧೦ ದಿನಗಳಿಂದ ಕುಡಿಯುವ ನೀರು ಬರುತ್ತಿಲ್ಲ. ದಯವಿಟ್ಟು ನೀರಿನ ಸಮಸ್ಯೆಯನ್ನು ಪರಿಹರಿಸಿ.",
                "detected_language": "kn",
                "english_translation": "There is no drinking water in Indiranagar for the last 10 days. Please resolve the water issue.",
                "sector": "water",
                "specific_issue": "Total lack of drinking water supply",
                "urgency_score": 5.0,
                "sentiment": "negative",
                "pii_redacted_text": "There is no drinking water in Indiranagar for the last 10 days. Please resolve the water issue.",
                "cluster_id": 1,
                "reported_at": "2026-08-20T10:15:00"
            },
            {
                "id": 2,
                "raw_text": "Drinking water pipe leakage has resulted in zero water pressure. No water for our daily chores in Indiranagar.",
                "detected_language": "en",
                "english_translation": "Drinking water pipe leakage has resulted in zero water pressure. No water for our daily chores in Indiranagar.",
                "sector": "water",
                "specific_issue": "Pipeline leak causing supply failure",
                "urgency_score": 4.5,
                "sentiment": "negative",
                "pii_redacted_text": "Drinking water pipe leakage has resulted in zero water pressure. No water for our daily chores in Indiranagar.",
                "cluster_id": 1,
                "reported_at": "2026-08-20T11:45:00"
            },
            {
                "id": 3,
                "raw_text": "ಕೋರಮಂಗಲ ೮೦ ಅಡಿ ರಸ್ತೆಯಲ್ಲಿ ಭಾರಿ ಗುಂಡಿಗಳಿವೆ. ದ್ವಿಚಕ್ರ ವಾಹನ ಸವಾರರು ಬಿದ್ದು ಗಾಯಗೊಳ್ಳುತ್ತಿದ್ದಾರೆ.",
                "detected_language": "kn",
                "english_translation": "There are huge potholes on Koramangala 80 Feet Road. Two-wheeler riders are falling and getting injured.",
                "sector": "roads",
                "specific_issue": "Dangerous potholes on main arterial road",
                "urgency_score": 4.5,
                "sentiment": "negative",
                "pii_redacted_text": "There are huge potholes on Koramangala 80 Feet Road. Two-wheeler riders are falling and getting injured.",
                "cluster_id": 2,
                "reported_at": "2026-08-21T08:30:00"
            },
            {
                "id": 4,
                "raw_text": "The potholes on Koramangala 80 feet road are getting worse everyday. Commuting has become a nightmare.",
                "detected_language": "en",
                "english_translation": "The potholes on Koramangala 80 feet road are getting worse everyday. Commuting has become a nightmare.",
                "sector": "roads",
                "specific_issue": "Severe road damage and potholes",
                "urgency_score": 4.0,
                "sentiment": "negative",
                "pii_redacted_text": "The potholes on Koramangala 80 feet road are getting worse everyday. Commuting has become a nightmare.",
                "cluster_id": 2,
                "reported_at": "2026-08-21T09:15:00"
            },
            {
                "id": 5,
                "raw_text": "HSR layout sector 3 garbage pile is not cleared. Very bad smell and mosquito breeding.",
                "detected_language": "en",
                "english_translation": "HSR layout sector 3 garbage pile is not cleared. Very bad smell and mosquito breeding.",
                "sector": "sanitation",
                "specific_issue": "Uncleared waste heap and disease vector risk",
                "urgency_score": 3.4,
                "sentiment": "negative",
                "pii_redacted_text": "HSR layout sector 3 garbage pile is not cleared. Very bad smell and mosquito breeding.",
                "cluster_id": 3,
                "reported_at": "2026-08-22T07:50:00"
            },
            {
                "id": 6,
                "raw_text": "Severe shortage of clean drinking water and essential medicines in Hiriyur PHC.",
                "detected_language": "en",
                "english_translation": "Severe shortage of clean drinking water and essential medicines in Hiriyur PHC.",
                "sector": "health",
                "specific_issue": "Shortage of essential medical supplies",
                "urgency_score": 4.5,
                "sentiment": "negative",
                "pii_redacted_text": "Severe shortage of clean drinking water and essential medicines in Hiriyur PHC.",
                "cluster_id": 4,
                "reported_at": "2026-08-23T12:10:00"
            }
        ]

    def get_overview(self) -> Dict[str, Any]:
        return {
            "total_citizen_reports": 24,
            "total_sanctioned_expenditure": 48500000.0,
            "unserved_gaps_count": 3,
            "stalled_projects_count": 2,
            "stalled_capital_amount": 12500000.0,
            "sectors_breakdown": {
                "water": 10,
                "roads": 8,
                "sanitation": 4,
                "health": 2
            }
        }

    def get_priorities(self, sector: Optional[str] = None, verdict: Optional[str] = None) -> List[Dict[str, Any]]:
        results = self._priorities
        if sector:
            results = [p for p in results if p["sector"] == sector]
        if verdict:
            results = [p for p in results if p["verdict"] == verdict]
        return sorted(results, key=lambda x: x["score"], reverse=True)

    def get_priority_detail(self, priority_id: int) -> Optional[Dict[str, Any]]:
        return self._priority_details.get(priority_id)

    def get_clusters(self, sector: Optional[str] = None, region_id: Optional[int] = None) -> List[Dict[str, Any]]:
        results = self._clusters
        if sector:
            results = [c for c in results if c["sector"] == sector]
        if region_id is not None:
            results = [c for c in results if c["region_id"] == region_id]
        return sorted(results, key=lambda x: x["report_count"], reverse=True)

    def get_cluster_detail(self, cluster_id: int) -> Optional[Dict[str, Any]]:
        cluster = next((c for c in self._clusters if c["id"] == cluster_id), None)
        if not cluster:
            return None
        return {
            **cluster,
            "reports": [r for r in self._reports if r["cluster_id"] == cluster_id],
            "expenditures": []
        }

    def get_reports(self, sector: Optional[str] = None, limit: int = 20, offset: int = 0) -> Dict[str, Any]:
        reports = self._reports
        if sector:
            reports = [r for r in reports if r["sector"] == sector]
        total = len(reports)
        paged = reports[offset : offset + limit]
        return {
            "total": total,
            "limit": limit,
            "offset": offset,
            "reports": paged
        }

    def get_report_detail(self, report_id: int) -> Optional[Dict[str, Any]]:
        return next((r for r in self._reports if r["id"] == report_id), None)

    def get_tracking_report(self, tracking_id: str) -> Optional[Dict[str, Any]]:
        for r in self._reports:
            if r.get("tracking_id") == tracking_id:
                return {
                    "tracking_id": tracking_id,
                    "sector": r["sector"],
                    "status": "received",
                    "reported_at": r["reported_at"],
                    "channel": "web",
                    "cluster_id": r.get("cluster_id")
                }
        return None

    def get_regions(self, level: Optional[str] = None, parent_id: Optional[int] = None) -> List[Dict[str, Any]]:
        results = self._regions
        if level:
            results = [r for r in results if r["level"] == level]
        if parent_id is not None:
            results = [r for r in results if r["parent_id"] == parent_id]
        return results

    def get_region_detail(self, region_id: int) -> Optional[Dict[str, Any]]:
        return next((r for r in self._regions if r["id"] == region_id), None)

    def get_expenditures(self, sector: Optional[str] = None, region_id: Optional[int] = None) -> List[Dict[str, Any]]:
        exps = [
            {
                "id": 1,
                "title": "Pothole Remediation & Asphalt Overlays - Koramangala 80 Feet Rd",
                "sector": "roads",
                "amount": 4500000.0,
                "status": "stalled",
                "allocated_year": 2025,
                "region_id": 4,
                "region_name": "Koramangala Ward"
            },
            {
                "id": 2,
                "title": "Borewell Water Treatment & RO Plant",
                "sector": "water",
                "amount": 2500000.0,
                "status": "completed",
                "allocated_year": 2025,
                "region_id": 5,
                "region_name": "HSR Layout Ward"
            },
            {
                "id": 3,
                "title": "Arterial Street Lighting & Drainage Repair",
                "sector": "roads",
                "amount": 1200000.0,
                "status": "in_progress",
                "allocated_year": 2025,
                "region_id": 3,
                "region_name": "Indiranagar Ward"
            }
        ]
        if sector:
            exps = [e for e in exps if e["sector"] == sector]
        if region_id is not None:
            exps = [e for e in exps if e["region_id"] == region_id]
        return exps

    def run_simulation(self, available_budget: float, strategy: str = "equity") -> Dict[str, Any]:
        priorities = self.get_priorities()
        allocations = []
        spent = 0.0
        gaps_resolved = 0
        needs_addressed = 0

        # Sort based on strategy
        if strategy == "reach":
            sorted_p = sorted(priorities, key=lambda x: x["report_count"], reverse=True)
        else:
            sorted_p = sorted(priorities, key=lambda x: x["score"], reverse=True)

        for p in sorted_p:
            detail = self.get_priority_detail(p["id"])
            cost = 3500000.0
            if detail and "evidence_bundle" in detail:
                cost = detail["evidence_bundle"].get("estimated_cost", 3500000.0)

            remaining = available_budget - spent
            if remaining <= 0:
                break

            if remaining >= cost:
                allocated = cost
                status = "fully_funded"
                pct = 100.0
                gaps_resolved += 1
                needs_addressed += p["report_count"]
            else:
                allocated = remaining
                status = "partially_funded"
                pct = round((allocated / cost) * 100, 1)
                needs_addressed += int(p["report_count"] * (allocated / cost))

            spent += allocated
            allocations.append({
                "cluster_id": p["cluster_id"],
                "title": p["title"],
                "sector": p["sector"],
                "allocated_amount": allocated,
                "pct_funded": pct,
                "status": status
            })

        return {
            "strategy": strategy,
            "simulated_budget": available_budget,
            "total_spent": spent,
            "remaining_budget": max(0.0, available_budget - spent),
            "gaps_fully_resolved": gaps_resolved,
            "citizen_needs_addressed": needs_addressed,
            "allocations": allocations
        }

demo_store = DemoStore()
