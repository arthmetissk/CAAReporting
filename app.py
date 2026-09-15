from flask import Flask, render_template, request, redirect, session, jsonify, send_from_directory
from pathlib import Path
import os
import re

from campaign_knowledge import (
    AUGUST_CAMPAIGNS,
    RECOMMENDATIONS,
    SUMMARY_HIGHLIGHTS,
    CHAT_SUGGESTIONS,
    STORES,
    MONTHLY_STORIES,
    reports_for_ui,
    all_campaigns_for_ui,
    families_for_ui,
    months_for_ui,
    full_knowledge_text,
    answer_from_knowledge,
    executive_summary_answer,
    store_labels,
    campaign_by_id,
)

app = Flask(__name__)
# Render sometimes leaves SECRET_KEY blank after secret edits; empty string disables sessions
# and makes POST /login return 500 when writing the auth cookie.
app.secret_key = os.getenv("SECRET_KEY") or "caa-secret-key-2026"

WORKSPACE = Path(__file__).resolve().parent
REPORT_DIR = WORKSPACE
ALL_CAMPAIGNS_DIR = WORKSPACE / "All Campaigns"
SUMMARY_FILE = WORKSPACE / "CAA_August2026_Campaign_Summary.html"
AUGUST_SUMMARY_IN_ARCHIVE = ALL_CAMPAIGNS_DIR / "2026_August_CAA_Campaign_Summary.html"

APP_USERNAME = (os.getenv("APP_USERNAME") or "caa").strip()
APP_PASSWORD = (os.getenv("APP_PASSWORD") or "twinleaf1234").strip()
ANTHROPIC_API_KEY = (os.getenv("ANTHROPIC_API_KEY") or "").strip() or None
CHAT_MODEL = (os.getenv("CHAT_MODEL") or "claude-3-5-sonnet-20241022").strip()

REPORTS = reports_for_ui()
ALL_CAMPAIGN_CARDS = all_campaigns_for_ui()
FAMILY_CARDS = families_for_ui()
MONTH_CARDS = months_for_ui()

MONTHLY_SUMMARIES = [
    {
        "slug": m["slug"],
        "month": m["month"],
        "filename": m["filename"],
        "theme": m["theme"],
        "objective": m["recommendations"][0] if m.get("recommendations") else m["theme"],
        "summary": m["summary"],
        "brand": " + ".join(m["brands"]),
        "stores": m["stores"],
        "reports": [campaign_by_id(cid)["filename"] for cid in m["campaign_ids"] if campaign_by_id(cid)],
        "highlights": m["highlights"],
        "metrics": m["metrics"],
        "status": m["status"],
    }
    for m in MONTHLY_STORIES
]

STORY_MONTHS = [
    {"month": "May", "theme": "Loyalty registration and trial mechanics", "campaigns": ["Pizza/Gas Loyalty (Twinleaf)", "Thunder Ice Cream (Twinleaf)", "Game Cigarillos (SW)", "Fireworks Summer Promo Projection (SW)"], "insight": "May established the customer base and offer patterns that lead later into summer loyalty and creative loops."},
    {"month": "June", "theme": "Fireworks and loyalty stretch into June", "campaigns": ["Fireworks June (SW)", "Sandwich Deal (Twinleaf)", "Breakfast Coffee Combo (Twinleaf)", "Smart Water (Twinleaf)"], "insight": "June connected activation events with reward mechanics and started identifying the strongest cross-category repetition signals."},
    {"month": "July", "theme": "Summer loyalty expansion and platform-building", "campaigns": ["Summer Cooler Deal (Twinleaf)", "ZYN BuyDown (SW)", "BeatHeat loyalty (Twinleaf)", "Promotions Summary"], "insight": "July deepened the seasonal rhythm; the campaign family widened from localized offers into broad dollar and loyalty behavior comparisons."},
    {"month": "August", "theme": "August campaign intelligence summary", "campaigns": ["Fireworks (SW1/SW2)", "Vape Loyalty (SW1/SW2)", "FoodToGo (TXP/TGC)", "Bagel Coffee Combo (TXP/TGC)"], "insight": "August confirms that the strongest story is loyalty-driven behavior that produces repeat frequency and more disciplined product relevance."},
]

INTERRELATED_CAMPAIGNS = [
    {"family": "Loyalty and breakfast bundles", "brand": "Twinleaf", "stores": ["TXP", "TGC"], "reports": ["2026_May_38_Breakfast_Coffee_Combo_Loyalty_Promo_Twinleaf.html", "2026_June_38_Breakfast_Coffee_Combo_Loyalty_Promo_Twinleaf.html", "2026_July_38d_Breakfast_Coffee_Combo_Loyalty_Promo_Twinleaf.html"], "summary": "Twinleaf breakfast/coffee bundle family carries a consistent loyalty story from May into July across Express and Gas & Convenience."},
    {"family": "Sandwich deal loyalty mechanics", "brand": "Twinleaf", "stores": ["TXP", "TGC"], "reports": ["2026_May_37_Sandwich_Deal_Loyalty_Promo_Twinleaf.html", "2026_June_37_Sandwich_Deal_Loyalty_Promo_Twinleaf.html", "2026_July_37d_Sandwich_Deal_Loyalty_Promo_Twinleaf.html"], "summary": "Twinleaf sandwich loyalty shows a multi-month offer ladder where repeat meal occasions move with carded behavior."},
    {"family": "Fireworks and seasonal summer programs", "brand": "Smokers Warehouse", "stores": ["SW1", "SW2"], "reports": ["2026_May_35_Fireworks_Promo_Smokers_Warehouse.html", "2026_June_41_Fireworks_June_2026_Campaign_Performance.html", "2026_August_41f_Fireworks_Campaign.html"], "summary": "Smokers Warehouse fireworks should be judged on summer peak (June/July), not August clearance economics."},
]

CAMPAIGN_MONTHLY_STORY = [
    {
        "month": "May 2026",
        "theme": "Loyalty foundations",
        "summary": "The campaign story starts with loyalty registration and offer design. Twinleaf leads food/gas loops; Smokers Warehouse runs seasonal tobacco activations.",
        "campaigns": [
            {"name": "Pizza & Gas Loyalty", "type": "Continuous", "status": "Active family", "objective": "Build carded customer repeat behavior.", "brand": "Twinleaf", "stores": ["TXP", "TGC"]},
            {"name": "Sandwich Deal Loyalty", "type": "Continuous", "status": "Active family", "objective": "Create repeat meal occasion behavior.", "brand": "Twinleaf", "stores": ["TXP", "TGC"]},
            {"name": "Breakfast Coffee Combo", "type": "Continuous", "status": "Active family", "objective": "Link breakfast and coffee category intent.", "brand": "Twinleaf", "stores": ["TXP", "TGC"]},
            {"name": "Thunder Ice Cream", "type": "One-off", "status": "Seasonal burst", "objective": "Create summer trial behavior.", "brand": "Twinleaf", "stores": ["TXP", "TGC"]},
            {"name": "Game Cigarillos", "type": "One-off", "status": "Activation", "objective": "Promote category conversion.", "brand": "Smokers Warehouse", "stores": ["SW1", "SW2"]},
        ],
    },
    {
        "month": "June 2026",
        "theme": "Activation and scale",
        "summary": "June extends Twinleaf loyalty themes and strengthens Smokers Warehouse summer event logic.",
        "campaigns": [
            {"name": "Sandwich Deal Loyalty", "type": "Continuous", "status": "Active family", "objective": "Repeat meal deal behavior.", "brand": "Twinleaf", "stores": ["TXP", "TGC"]},
            {"name": "Breakfast Coffee Combo", "type": "Continuous", "status": "Active family", "objective": "Bundle drink and food loop.", "brand": "Twinleaf", "stores": ["TXP", "TGC"]},
            {"name": "Fireworks June", "type": "One-off", "status": "Seasonal activation", "objective": "Seasonal awareness and store traffic.", "brand": "Smokers Warehouse", "stores": ["SW1", "SW2"]},
            {"name": "Smart Water 2-for-5", "type": "One-off", "status": "Trade promotion", "objective": "Category lift and shopper trial.", "brand": "Twinleaf", "stores": ["TXP", "TGC"]},
        ],
    },
    {
        "month": "July 2026",
        "theme": "Summer offer acceleration",
        "summary": "July turns the mix into a broader summer story across Twinleaf heat/cooler offers and Smokers Warehouse category buy-downs.",
        "campaigns": [
            {"name": "Summer Cooler Deal", "type": "One-off", "status": "Seasonal deal", "objective": "Grow summer category relevance.", "brand": "Twinleaf", "stores": ["TXP", "TGC"]},
            {"name": "ZYN BuyDown", "type": "One-off", "status": "Category activation", "objective": "Drive category trial and trade behavior.", "brand": "Smokers Warehouse", "stores": ["SW1", "SW2"]},
            {"name": "BeatHeat Loyalty", "type": "Continuous", "status": "Active family", "objective": "Protect consumer loyalty across heat occasions.", "brand": "Twinleaf", "stores": ["TXP", "TGC"]},
            {"name": "Breakfast Coffee Combo", "type": "Continuous", "status": "Active family", "objective": "Retain breakfast and coffee consistency.", "brand": "Twinleaf", "stores": ["TXP", "TGC"]},
        ],
    },
    {
        "month": "August 2026",
        "theme": "Optimization and learning",
        "summary": "August measurement split is clear: Smokers Warehouse = Vape + Fireworks; Twinleaf = Grab N Go + Bagel/Coffee.",
        "campaigns": [
            {"name": "Fireworks Campaign", "type": "One-off", "status": "Seasonal activation", "objective": "Seasonal reach and basket intent.", "brand": "Smokers Warehouse", "stores": ["SW1", "SW2"]},
            {"name": "Vape Loyalty Campaign", "type": "Continuous", "status": "Active family", "objective": "Retention through category loyalty.", "brand": "Smokers Warehouse", "stores": ["SW1", "SW2"]},
            {"name": "FoodToGo Loyalty", "type": "Continuous", "status": "Active family", "objective": "Meal occasion repeat conversion.", "brand": "Twinleaf", "stores": ["TXP", "TGC"]},
            {"name": "Bagel Coffee Combo", "type": "Continuous", "status": "Bundle family", "objective": "Bundle store visit and frequency behavior.", "brand": "Twinleaf", "stores": ["TXP", "TGC"]},
        ],
    },
]


def report_lookup():
    return {r["id"]: r for r in ALL_CAMPAIGN_CARDS}


def template_context():
    return {
        "reports": REPORTS,
        "all_campaigns": ALL_CAMPAIGN_CARDS,
        "families": FAMILY_CARDS,
        "month_cards": MONTH_CARDS,
        "recommendations": RECOMMENDATIONS,
        "highlights": SUMMARY_HIGHLIGHTS,
        "story_months": STORY_MONTHS,
        "interrelated_campaigns": INTERRELATED_CAMPAIGNS,
        "monthly_summaries": MONTHLY_SUMMARIES,
        "campaign_monthly_story": CAMPAIGN_MONTHLY_STORY,
        "chat_suggestions": CHAT_SUGGESTIONS,
        "stores": STORES,
        "executive_blurb": executive_summary_answer(),
    }


@app.before_request
def require_login():
    allowed = ["/login", "/static", "/favicon.ico", "/api/healthcheck"]
    if request.path.startswith(tuple(allowed)):
        return None
    if not session.get("authenticated"):
        return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        if username == APP_USERNAME and password == APP_PASSWORD:
            session["authenticated"] = True
            session["username"] = username
            return redirect("/")
        return render_template("login.html", error="Invalid username or password.")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


@app.route("/")
def dashboard():
    return render_template("index.html", **template_context())


@app.route("/month-story")
def month_story():
    return render_template("month_story.html", **template_context())


def safe_campaign_file(filename: str):
    """Resolve a report only if it stays inside All Campaigns."""
    if not filename or Path(filename).name != filename:
        return None
    file_path = (ALL_CAMPAIGNS_DIR / filename).resolve()
    try:
        file_path.relative_to(ALL_CAMPAIGNS_DIR.resolve())
    except ValueError:
        return None
    return file_path if file_path.is_file() else None


@app.route("/monthly-summary/<month_slug>")
def monthly_summary(month_slug):
    month = next((m for m in MONTHLY_SUMMARIES if m["slug"] == month_slug), None)
    if not month:
        return "Monthly summary not found", 404
    file_path = safe_campaign_file(month["filename"])
    if file_path:
        return send_from_directory(ALL_CAMPAIGNS_DIR, file_path.name)
    return "Monthly summary not found", 404


@app.route("/summary-report")
def summary_report():
    if AUGUST_SUMMARY_IN_ARCHIVE.is_file():
        return send_from_directory(ALL_CAMPAIGNS_DIR, AUGUST_SUMMARY_IN_ARCHIVE.name)
    if SUMMARY_FILE.is_file():
        return send_from_directory(REPORT_DIR, SUMMARY_FILE.name)
    return "Summary report not found", 404


@app.route("/shared-report/<path:filename>")
def shared_report(filename):
    file_path = safe_campaign_file(Path(filename).name)
    if file_path:
        return send_from_directory(ALL_CAMPAIGNS_DIR, file_path.name)
    return "Shared report not found", 404


@app.route("/support-report/<report_id>")
def support_report(report_id):
    report = report_lookup().get(report_id)
    if not report:
        return "Report not found", 404
    file_path = safe_campaign_file(report["filename"])
    if file_path:
        return send_from_directory(ALL_CAMPAIGNS_DIR, file_path.name)
    root_fallback = REPORT_DIR / report["filename"]
    # Also try root-level August copies
    august_root = {
        "fireworks": "41f_August2026_Fireworks_Campaign.html",
        "vape-loyalty": "41g_August2026_Vape_Loyalty_Campaign.html",
        "foodtogoto": "41h_August2026_FoodToGo_Loyalty_Campaign.html",
        "bagelcoffee": "41i_August2026_BagelCoffeeCombo_Snapshot.html",
    }.get(report_id)
    if august_root and (REPORT_DIR / august_root).is_file():
        return send_from_directory(REPORT_DIR, august_root)
    if root_fallback.is_file():
        return send_from_directory(REPORT_DIR, root_fallback.name)
    return "Report not found", 404


@app.route("/api/reports")
def api_reports():
    return jsonify({"reports": REPORTS, "all_campaigns": ALL_CAMPAIGN_CARDS, "stores": STORES})


@app.route("/api/browse")
def api_browse():
    """Filter campaigns by month, store, family, or campaign id."""
    month = (request.args.get("month") or "").strip().lower()
    store = (request.args.get("store") or "").strip().upper()
    family = (request.args.get("family") or "").strip().lower()
    campaign_id = (request.args.get("campaign") or "").strip().lower()

    items = ALL_CAMPAIGN_CARDS
    if campaign_id:
        items = [c for c in items if c["id"] == campaign_id]
    if month:
        items = [c for c in items if c["month_slug"] == month or c["month"].lower().startswith(month)]
    if store:
        items = [c for c in items if store in c["stores"]]
    if family:
        items = [c for c in items if c.get("family") == family]

    return jsonify({
        "filters": {"month": month, "store": store, "family": family, "campaign": campaign_id},
        "count": len(items),
        "campaigns": items,
        "months": MONTH_CARDS,
        "families": FAMILY_CARDS,
        "stores": STORES,
    })


@app.route("/api/recommendations")
def api_recommendations():
    return jsonify({"recommendations": RECOMMENDATIONS})


@app.route("/api/summary")
def api_summary():
    return jsonify({
        "summary": executive_summary_answer(),
        "highlights": SUMMARY_HIGHLIGHTS,
        "campaigns": REPORTS,
        "recommendations": RECOMMENDATIONS,
    })


@app.route("/api/chat", methods=["POST"])
def api_chat():
    data = request.get_json(silent=True) or {}
    query = (data.get("query") or "").strip()
    if not query:
        return jsonify({
            "answer": "Try a suggested question below, or ask about a month, store, or campaign family.",
            "formatted": {
                "headline": "Ask about CAA campaign results",
                "bullets": [
                    "Summarize a month (May–August)",
                    "Review a continuous family (sandwich, free coffee, fireworks)",
                    "Compare stores (SW1, SW2, TXP, TGC)",
                ],
                "next_step": None,
            },
            "recommendations": RECOMMENDATIONS[:2],
            "metrics": [],
            "campaigns": [],
            "suggestions": CHAT_SUGGESTIONS,
        })

    answer, campaigns, recs = generate_chat_payload(query)
    metrics = []
    for c in campaigns[:2]:
        for m in c.get("metrics", [])[:3]:
            metrics.append({
                "campaign": c["title"],
                "brand": c.get("brand"),
                "stores": store_labels(c.get("stores", [])),
                **m,
            })

    formatted = structure_chat_answer(answer, recs)

    return jsonify({
        "answer": answer,
        "formatted": formatted,
        "recommendations": recs,
        "metrics": metrics,
        "campaigns": [
            {
                "id": c["id"],
                "title": c["title"],
                "brand": c.get("brand"),
                "stores": store_labels(c.get("stores", [])),
                "status": c.get("status"),
            }
            for c in campaigns[:3]
        ],
        "suggestions": CHAT_SUGGESTIONS,
    })


@app.route("/api/healthcheck")
def healthcheck():
    archive_count = len(list(ALL_CAMPAIGNS_DIR.glob("*.html"))) if ALL_CAMPAIGNS_DIR.is_dir() else 0
    return jsonify({
        "status": "ok",
        "reports": len(REPORTS),
        "monthly_summaries": len(MONTHLY_SUMMARIES),
        "archive_html_files": archive_count,
        "chat_enabled": bool(ANTHROPIC_API_KEY),
        "secret_key_configured": bool(app.secret_key),
    })


def generate_chat_payload(query):
    """Prefer grounded knowledge; optionally refine with Anthropic using the same facts."""
    grounded_answer, campaigns, recs = answer_from_knowledge(query)

    if ANTHROPIC_API_KEY:
        try:
            from anthropic import Anthropic
            client = Anthropic(api_key=ANTHROPIC_API_KEY)
            response = client.messages.create(
                model=CHAT_MODEL,
                max_tokens=360,
                temperature=0.1,
                system=(
                    "You are CAA's campaign analyst. Never invent metrics. "
                    "Respond in this exact layout:\n"
                    "HEADLINE: <one clear sentence>\n"
                    "POINTS:\n"
                    "- <metric-backed point with brand/stores>\n"
                    "- <metric-backed point>\n"
                    "- <metric-backed point>\n"
                    "NEXT: <one concrete recommendation>\n"
                    "Keep each point under 25 words."
                ),
                messages=[{
                    "role": "user",
                    "content": (
                        full_knowledge_text()
                        + "\n\nDraft grounded answer:\n"
                        + grounded_answer
                        + "\n\nUser question: "
                        + query
                    ),
                }],
            )
            text = []
            for block in getattr(response, "content", []):
                if hasattr(block, "text"):
                    text.append(block.text)
            if text:
                return "\n".join(text).strip(), campaigns, recs
        except Exception:
            pass

    return grounded_answer, campaigns, recs


def structure_chat_answer(answer, recs):
    """Turn free text into a clean headline / bullets / next-step card."""
    raw = (answer or "").strip()
    if not raw:
        return {"headline": "No answer available.", "bullets": [], "next_step": None}

    # Structured Anthropic layout
    if re.search(r"(?im)^HEADLINE:", raw):
        headline_m = re.search(r"(?im)^HEADLINE:\s*(.+)$", raw)
        next_m = re.search(r"(?im)^NEXT:\s*(.+)$", raw)
        points = re.findall(r"(?im)^(?:-|\*|•)\s*(.+)$", raw)
        return {
            "headline": (headline_m.group(1).strip() if headline_m else raw.splitlines()[0]),
            "bullets": [p.strip() for p in points if p.strip()][:6],
            "next_step": (next_m.group(1).strip() if next_m else None),
        }

    # Fallback: split dense paragraphs into readable bullets
    text = clean_chat_text(raw)
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
    headline = sentences[0] if sentences else text
    bullets = sentences[1:] if len(sentences) > 1 else []

    next_step = None
    action_words = ("recommend", "next", "re-run", "shift", "fix", "add", "keep", "plan", "protect", "move")
    if bullets and any(w in bullets[-1].lower() for w in action_words):
        next_step = bullets[-1]
        bullets = bullets[:-1]
    elif recs:
        first = recs[0]
        next_step = first.get("title") if isinstance(first, dict) else str(first)

    # Prefer shorter bullets when a sentence is very long
    compact = []
    for b in bullets[:6]:
        if len(b) > 180 and " — " in b:
            compact.extend([p.strip() for p in b.split(" — ") if p.strip()][:2])
        else:
            compact.append(b)

    return {
        "headline": headline,
        "bullets": compact[:5],
        "next_step": next_step,
    }


def clean_chat_text(text):
    text = text.replace("\n", " ")
    return re.sub(r"\s+", " ", text).strip()


# Back-compat for tests
def generate_chat_answer(query):
    answer, _, _ = generate_chat_payload(query)
    return answer


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=False)
