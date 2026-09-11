from flask import Flask, render_template, request, redirect, url_for, session, jsonify, send_from_directory
from pathlib import Path
import os
import re

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "caa-secret-key-2026")

WORKSPACE = Path(__file__).resolve().parent
REPORT_DIR = WORKSPACE
SUMMARY_FILE = WORKSPACE / "CAA_August2026_Campaign_Summary.html"

APP_USERNAME = os.getenv("APP_USERNAME", "caa")
APP_PASSWORD = os.getenv("APP_PASSWORD", "twinleaf1234")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

REPORTS = [
    {"id": "fireworks", "filename": "41f_August2026_Fireworks_Campaign.html", "title": "Fireworks Campaign", "category": "Seasonal activation", "summary": "High-impact seasonal campaign with storefront uplift and audience expansion."},
    {"id": "vape-loyalty", "filename": "41g_August2026_Vape_Loyalty_Campaign.html", "title": "Vape Loyalty Campaign", "category": "Loyalty & retention", "summary": "Retention program measured against repeat visit and wallet depth."},
    {"id": "foodtogoto", "filename": "41h_August2026_FoodToGo_Loyalty_Campaign.html", "title": "FoodToGo Loyalty Campaign", "category": "On-the-go food", "summary": "Food-to-go behavior, offer activation, and repeat conversion analysis."},
    {"id": "bagelcoffee", "filename": "41i_August2026_BagelCoffeeCombo_Snapshot.html", "title": "Bagel Coffee Combo Snapshot", "category": "Bundle snapshot", "summary": "Cross-category breakfast bundle performance snapshot."},
]

SUMMARY_HIGHLIGHTS = [
    "Total campaign momentum is strongest where loyalty and bundles are activated together.",
    "Channel and offer selection should prioritize repeat-purchase behavior over one-off reach.",
    "Budget should continue to concentrate on performing placements and conversion loops.",
    "Storefront and digital creative should reinforce food and lifestyle category relevance.",
]

RECOMMENDATIONS = [
    {"title": "Scale performance bundles", "impact": "High", "detail": "Invest further in cross-sell bundles that combine food and beverage occasions."},
    {"title": "Double down on loyalty loops", "impact": "High", "detail": "Push retention programs that reward frequency and repeat purchase."},
    {"title": "Protect seasonal creative", "impact": "Medium", "detail": "Extend creative themes that made the campaign feel timely and locally relevant."},
    {"title": "Refine channel allocation", "impact": "Medium", "detail": "Move more budget toward outcomes that show strong conversion and repeat visits."},
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
    return render_template("index.html", reports=REPORTS, recommendations=RECOMMENDATIONS, highlights=SUMMARY_HIGHLIGHTS)


@app.route("/summary-report")
def summary_report():
    return send_from_directory(REPORT_DIR, SUMMARY_FILE.name)


@app.route("/support-report/<report_id>")
def support_report(report_id):
    report = report_lookup().get(report_id)
    if report:
        return send_from_directory(REPORT_DIR, report["filename"])
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
            response = client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=280,
                temperature=0.2,
                system="You are a campaign intelligence assistant. Respond in 2-4 sentences. Include a clear strategic insight and one next recommendation.",
                messages=[{ "role": "user", "content": f"Campaign files: {', '.join(r['title'] for r in REPORTS)}. User question: {query}" }]
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

    q = query.lower()
    # Strategic fallback using local report themes
    if "fireworks" in q or "seasonal" in q:
        return "Fireworks should be treated as a conversion-quality opportunity: protect seasonal creative and recommend a basket-building offer that raises visit value. Prioritize a bundle or add-on that turns one-time campaign reach into repeat spend."
    if "vape" in q or "loyalty" in q or "vape loyalty" in q:
        return "Vape Loyalty is the clearest win because cardholder revenue momentum and repeat behavior are moving together. Recommend scaling the offer logic that rewards repeat value and using the most precise customer segment to expand frequency."
    if "food" in q or "foodtog" in q or "food-to-go" in q:
        return "FoodToGo should improve feed through a tighter loyalty loop that rewards repeat meal decisions while maintaining basket discipline. Recommend a conversion offer that protects meal frequency without reducing average order value."
    if "bagel" in q or "coffee" in q or "combo" in q:
        return "The Bagel Coffee Combo signal suggests a cross-category bundle can create a practical discovery moment. Recommend pairing the bundle with a consistent loyalty message that deepens repeat coffee-and-bagel behavior."
    if "recommend" in q or "strategy" in q or "opportunity" in q:
        return "Recommend prioritizing loyalty loops that prove repeat purchase, scaling the strongest bundle mechanics, and moving budget toward channels with the best conversion and wallet expansion."

    return "The strongest strategic pattern is loyalty-driven conversion with higher repeat value. Recommend expanding the offer mix that proves repeat purchase behavior, protecting high-performing creative, and reallocating spend away from low-intent channels."


def clean_chat_text(text):
    text = text.replace("\n", " ")
    return re.sub(r"\s+", " ", text).strip()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=False)
