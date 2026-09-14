from flask import Flask, render_template, request, redirect, url_for, session, jsonify, send_from_directory
from pathlib import Path
import os
import re

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "caa-secret-key-2026")

WORKSPACE = Path(__file__).resolve().parent
REPORT_DIR = WORKSPACE
ALL_CAMPAIGNS_DIR = WORKSPACE.parent / "All Campaigns"
SUMMARY_FILE = WORKSPACE / "CAA_August2026_Campaign_Summary.html"

APP_USERNAME = os.getenv("APP_USERNAME", "caa")
APP_PASSWORD = os.getenv("APP_PASSWORD", "twinleaf1234")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

REPORTS = [
    {"id": "fireworks", "filename": "2026_August_41f_Fireworks_Campaign.html", "title": "Fireworks Campaign", "category": "Seasonal activation", "summary": "High-impact seasonal campaign with storefront uplift and audience expansion.", "folder": "All Campaigns"},
    {"id": "vape-loyalty", "filename": "2026_August_41g_Vape_Loyalty_Campaign.html", "title": "Vape Loyalty Campaign", "category": "Loyalty & retention", "summary": "Retention program measured against repeat visit and wallet depth.", "folder": "All Campaigns"},
    {"id": "foodtogoto", "filename": "2026_August_41h_FoodToGo_Loyalty_Campaign.html", "title": "FoodToGo Loyalty Campaign", "category": "On-the-go food", "summary": "Food-to-go behavior, offer activation, and repeat conversion analysis.", "folder": "All Campaigns"},
    {"id": "bagelcoffee", "filename": "2026_August_41i_BagelCoffeeCombo_Snapshot.html", "title": "Bagel Coffee Combo Snapshot", "category": "Bundle snapshot", "summary": "Cross-category breakfast bundle performance snapshot.", "folder": "All Campaigns"},
]

SUMMARY_HIGHLIGHTS = [
    "The strongest campaign signal is the way loyalty, frequency, and bundle behavior connect across the month-to-month story.",
    "Campaign growth is strongest when customers are moved from one-time reach into repeat purchase loops.",
    "The best-performing reports show that budget should continue to concentrate on creative, channels, and categories with repeat conversion evidence.",
    "The measurement story is clearer when promotions are grouped around shared audience, offer, and loyalty mechanics.",
]

MONTHLY_SUMMARIES = [
    {"slug": "may", "month": "May 2026", "filename": "2026_May_Main_Campaign_Performance_Summary.html", "theme": "Loyalty registration and trial mechanics", "objective": "Build a repeat conversion base using food, beverage, and seasonal offers.", "summary": "May establishes category relevance, trial mechanics, and campaign offer behavior that can scale into a repeat loyalty system.", "reports": ["2026_May_39_Pizza_Gas_Loyalty_Twinleaf.html", "2026_May_37_Sandwich_Deal_Loyalty_Promo_Twinleaf.html", "2026_May_38_Breakfast_Coffee_Combo_Loyalty_Promo_Twinleaf.html"]},
    {"slug": "june", "month": "June 2026", "filename": "2026_June_Main_Campaign_Performance_Summary.html", "theme": "Summer activation and reward stretch", "objective": "Extend the loyalty and seasonality rhythm into broader broadcast and offer testing.", "summary": "June connects activation, food behavior, drink offers, and regional campaign performance to create a stronger summer campaign narrative.", "reports": ["2026_June_41_Fireworks_June_2026_Campaign_Performance.html", "2026_June_44_Smart_Water_2for5_Campaign_Performance.html", "2026_June_37_Sandwich_Deal_Loyalty_Promo_Twinleaf.html"]},
    {"slug": "july", "month": "July 2026", "filename": "2026_July_Promotions_Summary.html", "theme": "Summer creative momentum and promotional acceleration", "objective": "Turn summer traffic into basket-building, reward-led loyalty behavior.", "summary": "July deepens the campaign vocabulary by pairing high-summer promotions with cross-category creative and warmer-weather deal logic.", "reports": ["2026_July_45_Summer_Cooler_Deal.html", "2026_July_47a_BeatHeat_Loyalty.html", "2026_July_46_ZYN_BuyDown_SW.html"]},
    {"slug": "august", "month": "August 2026", "filename": "2026_August_CAA_Campaign_Summary.html", "theme": "August campaign intelligence summary", "objective": "Create an optimized August measurement readout for loyalty, food, coffee, vape, and seasonal activation.", "summary": "August confirms the strongest campaign system is built around loyalty loops, category relevance, and repeat customer conversion.", "reports": ["2026_August_41f_Fireworks_Campaign.html", "2026_August_41g_Vape_Loyalty_Campaign.html", "2026_August_41h_FoodToGo_Loyalty_Campaign.html", "2026_August_41i_BagelCoffeeCombo_Snapshot.html"]},
]

RECOMMENDATIONS = [
    {"title": "Scale the loyalty bundle machine", "impact": "High", "detail": "Invest further in the cross-category loyalty and bundle patterns that create frequency and basket lift."},
    {"title": "Connect month-to-month creative and offer momentum", "impact": "High", "detail": "Carry forward the most effective seasonal and loyalty creative into each succeeding month narrative."},
    {"title": "Protect repeat purchase economics", "impact": "Medium", "detail": "Make repeat conversion and review cycle behavior a central requirement before adding new spend to underperforming reports."},
    {"title": "Reframe budget by campaign family", "impact": "Medium", "detail": "Compare customer movement across promotions, identify the most productive customer range, and reallocate spend by winning campaign family."},
]

STORY_MONTHS = [
    {"month": "May", "theme": "Loyalty registration and trial mechanics", "campaigns": ["Pizza/Gas Loyalty", "Thunder Ice Cream", "Game Cigarillos", "Fireworks Summer Promo Projection"], "insight": "May established the customer base and offer patterns that lead later into summer loyalty and creative loops."},
    {"month": "June", "theme": "Fireworks and loyalty stretch into June", "campaigns": ["Fireworks June", "Sandwich Deal", "Breakfast Coffee Combo", "Smart Water"], "insight": "June connected activation events with reward mechanics and started identifying the strongest cross-category repetition signals."},
    {"month": "July", "theme": "Summer loyalty expansion and platform-building", "campaigns": ["Summer Cooler Deal", "ZYN BuyDown", "BeatHeat loyalty", "Promotions Summary"], "insight": "July deepened the seasonal rhythm; the campaign family widened from localized offers into broad dollar and loyalty behavior comparisons."},
    {"month": "August", "theme": "August campaign intelligence summary", "campaigns": ["Fireworks", "Vape Loyalty", "FoodToGo", "Bagel Coffee Combo"], "insight": "August confirms that the strongest story is loyalty-driven behavior that produces repeat frequency and more disciplined product relevance."},
]

INTERRELATED_CAMPAIGNS = [
    {"family": "Loyalty and breakfast bundles", "reports": ["2026_May_38_Breakfast_Coffee_Combo_Loyalty_Promo_Twinleaf.html", "2026_June_38_Breakfast_Coffee_Combo_Loyalty_Promo_Twinleaf.html", "2026_July_38d_Breakfast_Coffee_Combo_Loyalty_Promo_Twinleaf.html"], "summary": "The breakfast and coffee bundle campaign family shows that loyalty offer design can be used to carry a consistent customer story from May into July."},
    {"family": "Sandwich deal loyalty mechanics", "reports": ["2026_May_37_Sandwich_Deal_Loyalty_Promo_Twinleaf.html", "2026_June_37_Sandwich_Deal_Loyalty_Promo_Twinleaf.html", "2026_July_37d_Sandwich_Deal_Loyalty_Promo_Twinleaf.html"], "summary": "The sandwich loyalty campaign demonstrates a multi-month offer ladder where loyalty behavior and repeat food occasions move together."},
    {"family": "Fireworks and seasonal summer programs", "reports": ["2026_May_35_Fireworks_Promo_Smokers_Warehouse.html", "2026_June_41_Fireworks_June_2026_Campaign_Performance.html", "2026_August_41f_Fireworks_Campaign.html"], "summary": "Fireworks and summer promotional behavior become more understandable as separate campaign moments that need conversion quality and basket economics instead of pure volume behavior."},
]

CAMPAIGN_MONTHLY_STORY = [
    {
        "month": "May 2026",
        "theme": "Loyalty foundations",
        "summary": "The campaign story starts with a loyalty registration and offer design pattern. The strongest continuity themes emerge through Restaurant and Gas category loyalty loops.",
        "campaigns": [
            {"name": "Pizza & Gas Loyalty", "type": "Continuous", "status": "Active family", "objective": "Build carded customer repeat behavior."},
            {"name": "Sandwich Deal Loyalty", "type": "Continuous", "status": "Active family", "objective": "Create repeat meal occasion behavior."},
            {"name": "Breakfast Coffee Combo", "type": "Continuous", "status": "Active family", "objective": "Link breakfast and coffee category intent."},
            {"name": "Thunder Ice Cream", "type": "One-off", "status": "Seasonal burst", "objective": "Create summer trial behavior."},
            {"name": "Game Cigarillos", "type": "One-off", "status": "Activation", "objective": "Promote category conversion."}
        ]
    },
    {
        "month": "June 2026",
        "theme": "Activation and scale",
        "summary": "June extends the loyalty themes and makes the summer event logic stronger. Fireworks and water promotions deepen connection to seasonal spend behavior.",
        "campaigns": [
            {"name": "Sandwich Deal Loyalty", "type": "Continuous", "status": "Active family", "objective": "Repeat meal deal behavior."},
            {"name": "Breakfast Coffee Combo", "type": "Continuous", "status": "Active family", "objective": "Bundle drink and food loop."},
            {"name": "Fireworks June", "type": "One-off", "status": "Seasonal activation", "objective": "Seasonal awareness and store traffic."},
            {"name": "Smart Water 2-for-5", "type": "One-off", "status": "Trade promotion", "objective": "Category lift and shopper trial."}
        ]
    },
    {
        "month": "July 2026",
        "theme": "Summer offer acceleration",
        "summary": "July turns the campaign mix into a more promotional summer story with higher frequency, improved heat and occasion relevance, and wider seasonal creative testing.",
        "campaigns": [
            {"name": "Summer Cooler Deal", "type": "One-off", "status": "Seasonal deal", "objective": "Grow summer category relevance."},
            {"name": "ZYN BuyDown", "type": "One-off", "status": "Category activation", "objective": "Drive category trial and trade behavior."},
            {"name": "BeatHeat Loyalty", "type": "Continuous", "status": "Active family", "objective": "Protect consumer loyalty across heat occasions."},
            {"name": "Breakfast Coffee Combo", "type": "Continuous", "status": "Active family", "objective": "Retain breakfast and coffee consistency."}
        ]
    },
    {
        "month": "August 2026",
        "theme": "Optimization and learning",
        "summary": "August summarizes the strongest campaign family patterns and confirms the shift toward loyalty, category fit, and repeat behavior measurement.",
        "campaigns": [
            {"name": "Fireworks Campaign", "type": "One-off", "status": "Seasonal activation", "objective": "Seasonal reach and basket intent."},
            {"name": "Vape Loyalty Campaign", "type": "Continuous", "status": "Active family", "objective": "Retention through category loyalty."},
            {"name": "FoodToGo Loyalty", "type": "Continuous", "status": "Active family", "objective": "Meal occasion repeat conversion."},
            {"name": "Bagel Coffee Combo", "type": "Continuous", "status": "Bundle family", "objective": "Bundle store visit and frequency behavior."}
        ]
    }
]


def report_lookup():
    return {r["id"]: r for r in REPORTS}


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
    return render_template("index.html", reports=REPORTS, recommendations=RECOMMENDATIONS, highlights=SUMMARY_HIGHLIGHTS, story_months=STORY_MONTHS, interrelated_campaigns=INTERRELATED_CAMPAIGNS, monthly_summaries=MONTHLY_SUMMARIES, campaign_monthly_story=CAMPAIGN_MONTHLY_STORY)


@app.route("/month-story")
def month_story():
    return render_template("month_story.html", reports=REPORTS, recommendations=RECOMMENDATIONS, highlights=SUMMARY_HIGHLIGHTS, story_months=STORY_MONTHS, interrelated_campaigns=INTERRELATED_CAMPAIGNS, monthly_summaries=MONTHLY_SUMMARIES, campaign_monthly_story=CAMPAIGN_MONTHLY_STORY)


@app.route("/monthly-summary/<month_slug>")
def monthly_summary(month_slug):
    month = next((m for m in MONTHLY_SUMMARIES if m["slug"] == month_slug), None)
    if month:
        return send_from_directory(ALL_CAMPAIGNS_DIR, month["filename"])
    return "Monthly summary not found", 404


@app.route("/summary-report")
def summary_report():
    return send_from_directory(REPORT_DIR, SUMMARY_FILE.name)


@app.route("/shared-report/<filename>")
def shared_report(filename):
    file_path = ALL_CAMPAIGNS_DIR / filename
    if file_path.exists():
        return send_from_directory(ALL_CAMPAIGNS_DIR, filename)
    return "Shared report not found", 404


@app.route("/support-report/<report_id>")
def support_report(report_id):
    report = report_lookup().get(report_id)
    if report:
        return send_from_directory(ALL_CAMPAIGNS_DIR, report["filename"])
    return "Report not found", 404


@app.route("/api/reports")
def api_reports():
    return jsonify({"reports": REPORTS})


@app.route("/api/recommendations")
def api_recommendations():
    return jsonify({"recommendations": RECOMMENDATIONS})


@app.route("/api/chat", methods=["POST"])
def api_chat():
    data = request.get_json(silent=True) or {}
    query = (data.get("query") or "").strip()
    if not query:
        return jsonify({"answer": "Ask about a campaign, report, category, channel, or recommendation theme.", "recommendations": RECOMMENDATIONS[:2]})
    return jsonify({"answer": generate_chat_answer(query), "recommendations": RECOMMENDATIONS[:3]})


@app.route("/api/healthcheck")
def healthcheck():
    return jsonify({"status": "ok", "reports": len(REPORTS)})


def generate_chat_answer(query):
    # Prefer Anthropic if API key exists, but always answer with a concise strategic fallback.
    if ANTHROPIC_API_KEY:
        try:
            from anthropic import Anthropic
            client = Anthropic(api_key=ANTHROPIC_API_KEY)
            report_titles = ", ".join(r["title"] for r in REPORTS)
            month_story = ", ".join(f"{m['month']}::{m['theme']}" for m in MONTHLY_SUMMARIES)
            prompt_text = (
                "Campaign files: " + report_titles + ". "
                "Campaign story: " + month_story + ". "
                "User question: " + query
            )
            response = client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=280,
                temperature=0.2,
                system="You are a campaign intelligence assistant. Review the campaign performance context and respond in 2-4 sentences. Include a clear strategic insight and one recommendation.",
                messages=[{ "role": "user", "content": prompt_text }]
            )
            if response:
                text = []
                for block in getattr(response, "content", []):
                    if hasattr(block, "text"):
                        text.append(block.text)
                if text:
                    return clean_chat_text(" ".join(text))
        except Exception:
            pass

    q = (query or "").lower()

    families = [f["family"] for f in INTERRELATED_CAMPAIGNS]

    # Key performance inference from the integrated campaign story and report family context.
    if any(term in q for term in ["performance", "perform", "campaign", "measure", "month", "summary", "revenue", "recommend"]):
        return (
            "Across the May-August campaign sequence, the strongest evidence is that loyalty, repeat purchase, and bundle mechanics create more durable performance than isolated one-off lifts. "
            "The campaign families with the clearest continuity are " + ", ".join(families[:2]) + ", while the strongest campaign actions remain tied to repeat frequency and category relevance. "
            "Prioritize expanding the repeat-loyalty offer logic and funding the campaign families that convert trial into repeat value."
        )

    if "fireworks" in q or "seasonal" in q:
        return "Fireworks should be reviewed as a campaign moment that needs conversion-quality support rather than pure volume delivery. The best next recommendation is to pair seasonal awareness with a basket-building offer that converts one-time store traffic into repeat spend."

    if "vape" in q or "loyalty" in q or "vape loyalty" in q:
        return "Vape Loyalty is the clearest repeat-value family in the current campaign story because loyalty momentum and category behavior are moving together. Review the customer segment that proves repeat behavior and scale the offer design that deepens product relevance and frequency."

    if "food" in q or "foodtog" in q or "food-to-go" in q or "foodtogo" in q:
        return "FoodToGo should be evaluated through a tighter meal-occasion loyalty loop that rewards repeat food decisions while keeping basket economics disciplined. The recommended action is to protect the high-frequency offer structure and measure reward pull against meal repeat conversion."

    if "bagel" in q or "coffee" in q or "combo" in q:
        return "The Bagel Coffee Combo pattern suggests a cross-category bundle is an effective discovery and frequency driver. Review whether the bundle creates a repeat coffee-and-food habit and then extend that mechanics into the stronger loyalty family."

    if "recommend" in q or "strategy" in q or "opportunity" in q:
        return "Review the month-by-month offer families and prioritize loyalty loops that prove repeat purchase, then scale the strongest bundle mechanics across the campaign family. Protect the creative and category combinations that turn campaign attention into repeat value and budget discipline."

    return "The campaign performance pattern is most coherent when reviewed as a connected month-by-month loyalty system rather than as a single August report. Review the strongest family loops across May-August, protect the creative and bundle mechanics that create repeat behavior, and move future budget toward the campaigns with the clearest repeat-value signal."


def clean_chat_text(text):
    text = text.replace("\n", " ")
    return re.sub(r"\s+", " ", text).strip()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=False)
