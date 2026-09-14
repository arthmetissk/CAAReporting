"""Structured August 2026 campaign knowledge for dashboard + chat."""

STORES = {
    "SW1": {"name": "Smokers Warehouse 1", "short": "SW1 Akwesasne", "brand": "Smokers Warehouse", "location": "Akwesasne"},
    "SW2": {"name": "Smokers Warehouse 2", "short": "SW2 Ft. Covington", "brand": "Smokers Warehouse", "location": "Ft. Covington"},
    "TXP": {"name": "Twinleaf Express", "short": "TXP Express", "brand": "Twinleaf", "location": "Express"},
    "TGC": {"name": "Twinleaf Gas & Convenience", "short": "TGC Gas & Conv.", "brand": "Twinleaf", "location": "Gas & Convenience"},
}

BRANDS = {
    "Smokers Warehouse": ["SW1", "SW2"],
    "Twinleaf": ["TXP", "TGC"],
}

AUGUST_CAMPAIGNS = [
    {
        "id": "vape-loyalty",
        "filename": "2026_August_41g_Vape_Loyalty_Campaign.html",
        "title": "Vape Loyalty Campaign",
        "category": "Loyalty & retention",
        "status": "Strong",
        "signal": 90,
        "brand": "Smokers Warehouse",
        "stores": ["SW1", "SW2"],
        "offer": "4× points on all vape purchases (loyalty only)",
        "period": "August 1–31, 2026",
        "summary": "Clearest August win: loyalty vape revenue +32% YoY while non-loyalty fell −29%.",
        "metrics": [
            {"label": "Total vape rev", "value": "$100,279", "delta": "+3.6% YoY"},
            {"label": "Loyalty rev", "value": "$68,492", "delta": "+32.0% YoY"},
            {"label": "Loyalty share", "value": "68.3%", "delta": "144 cards · 1,420 trips"},
            {"label": "Non-loyalty rev", "value": "$31,787", "delta": "−29.2% YoY"},
            {"label": "Summer vape", "value": "$377,809", "delta": "+14.0% YoY"},
        ],
        "store_breakdown": [
            {"store": "SW1", "detail": "$66,654 total · $45,365 loyalty · 82 cards · 927 trips", "delta": "+3.4%"},
            {"store": "SW2", "detail": "$33,625 total · $23,126 loyalty · 62 cards · 493 trips", "delta": "+4.1%"},
        ],
        "takeaway": "SW1 drives ~66% of combined vape revenue; SW2 grew slightly faster. Multiplier pulled enrolled customers deeper into category spend.",
        "recommendation": "Re-run Vape 4× Points in Q4, ideally tied to a new SKU or seasonal brand push.",
    },
    {
        "id": "fireworks",
        "filename": "2026_August_41f_Fireworks_Campaign.html",
        "title": "Fireworks Campaign",
        "category": "Seasonal activation",
        "status": "Context",
        "signal": 72,
        "brand": "Smokers Warehouse",
        "stores": ["SW1", "SW2"],
        "offer": "20% off remaining inventory + 3× points on fireworks (loyalty)",
        "period": "August 1–31, 2026",
        "summary": "August is clearance, not peak: Aug FW −55.7% YoY, but summer FW +49% YoY to $433k.",
        "metrics": [
            {"label": "Aug FW rev", "value": "$5,806", "delta": "−55.7% YoY"},
            {"label": "Summer FW", "value": "$433,069", "delta": "+49.0% YoY"},
            {"label": "Loyalty rev", "value": "$405", "delta": "7.0% share · 13 cards"},
            {"label": "FW baskets", "value": "92", "delta": "vs 128 Aug 2025"},
        ],
        "store_breakdown": [
            {"store": "SW1", "detail": "$2,924 · 52 baskets · loyalty $168 (6 cards)", "delta": "−65.0%"},
            {"store": "SW2", "detail": "$2,882 · 40 baskets · loyalty $237 (7 cards)", "delta": "−39.4%"},
        ],
        "takeaway": "SW1’s August drop was nearly double SW2’s. Demand peaks June/July; August clearance should not be used to judge summer campaign quality.",
        "recommendation": "Shift fireworks promotions to May–June 2027 with a Memorial Day loyalty multiplier.",
    },
    {
        "id": "foodtogoto",
        "filename": "2026_August_41h_FoodToGo_Loyalty_Campaign.html",
        "title": "FoodToGo / Grab N Go Loyalty",
        "category": "On-the-go food",
        "status": "Mixed",
        "signal": 74,
        "brand": "Twinleaf",
        "stores": ["TXP", "TGC"],
        "offer": "2× points on any Grab N Go purchase (loyalty only)",
        "period": "August 1–31, 2026",
        "summary": "Loyalty cards/trips up, but total Grab N Go −4.6% and avg basket −5.6%.",
        "metrics": [
            {"label": "Total Grab N Go", "value": "$109,603", "delta": "−4.6% YoY"},
            {"label": "Loyalty rev", "value": "$12,641", "delta": "+11.3% YoY"},
            {"label": "Loyalty share", "value": "11.5%", "delta": "was 9.9%"},
            {"label": "Loyalty cards", "value": "142", "delta": "+14.5% · 1,456 trips"},
            {"label": "Avg basket/trip", "value": "$8.68", "delta": "−5.6% YoY"},
        ],
        "store_breakdown": [
            {"store": "TXP", "detail": "72 cards · 886 trips (+32.4%) · $9.60 basket (−10.9%)", "delta": "frequency up, basket down"},
            {"store": "TGC", "detail": "70 cards · 570 trips (+0.7%) · $7.26 basket (−0.8%)", "delta": "trips flat, basket steady"},
        ],
        "takeaway": "Opposite store responses: TXP is frequency-driven with lighter baskets; TGC holds basket. No new Grab N Go loyalty enrollments — all 142 were returning buyers.",
        "recommendation": "Add a Grab N Go bundle mechanic to lift avg basket; launch POS enrollment prompts for non-loyalty buyers.",
    },
    {
        "id": "bagelcoffee",
        "filename": "2026_August_41i_BagelCoffeeCombo_Snapshot.html",
        "title": "Bagel Coffee Combo Snapshot",
        "category": "Bundle snapshot",
        "status": "Baseline",
        "signal": 64,
        "brand": "Twinleaf",
        "stores": ["TXP", "TGC"],
        "offer": "Bagel + Coffee for $4.99 (all customers)",
        "period": "August 1–31, 2026",
        "summary": "First tracked month: 334 bagels ($1,667) and 392 coffees ($526). TGC is the combo home.",
        "metrics": [
            {"label": "Bagel units", "value": "334", "delta": "$1,667 rev"},
            {"label": "Coffee units", "value": "392", "delta": "$526 rev"},
            {"label": "Same-basket combos", "value": "12", "delta": "TGC only"},
            {"label": "Non-loyalty share", "value": "~83%", "delta": "of purchases"},
        ],
        "store_breakdown": [
            {"store": "TXP", "detail": "150 bagels ($749) · 69 coffees ($79) · 0 same-basket combos", "delta": "POS fix needed"},
            {"store": "TGC", "detail": "184 bagels ($918) · 323 coffees ($447) · 12 confirmed combos", "delta": "natural home"},
        ],
        "takeaway": "TXP rings bagels and coffee separately, so combo measurement is incomplete. TGC sold ~5× more coffee and generated all confirmed combos.",
        "recommendation": "Fix TXP POS combo ringing; treat September as Month 1 clean baseline.",
    },
]

RECOMMENDATIONS = [
    {
        "title": "Re-run Vape 4× Points in Q4",
        "impact": "High",
        "timing": "Q4 Action",
        "stores": ["SW1", "SW2"],
        "brand": "Smokers Warehouse",
        "detail": "Highest-ROI August structure. Loyalty vape +32% YoY at 68.3% share. Pair with a new SKU or seasonal brand for holiday push.",
    },
    {
        "title": "Shift Fireworks promotions to May–June 2027",
        "impact": "High",
        "timing": "2027 Plan",
        "stores": ["SW1", "SW2"],
        "brand": "Smokers Warehouse",
        "detail": "Summer FW hit $433k (+49% YoY). August −56% is clearance, not failure. Launch around Memorial Day with a loyalty multiplier.",
    },
    {
        "title": "Add Grab N Go bundle to lift basket",
        "impact": "Medium",
        "timing": "Q4 Action",
        "stores": ["TXP", "TGC"],
        "brand": "Twinleaf",
        "detail": "Trips +17.9% but avg basket −5.6% to $8.68. Pair Grab N Go with Bagel+Coffee for a points-on-combo offer.",
    },
    {
        "title": "Fix Bagel+Coffee POS ring at TXP",
        "impact": "Medium",
        "timing": "Ops Fix",
        "stores": ["TXP"],
        "brand": "Twinleaf",
        "detail": "TXP cannot confirm combos today. Align cashier process so bagel+coffee ring together; September becomes first clean baseline.",
    },
    {
        "title": "POS loyalty enrollment for non-loyalty buyers",
        "impact": "High",
        "timing": "Sep Launch",
        "stores": ["SW1", "SW2", "TXP", "TGC"],
        "brand": "Both brands",
        "detail": "Non-loyalty is falling in Vape (−29.2%) and Grab N Go (−6.3%). Prompt enrollment at register while the customer is already buying.",
    },
]

SUMMARY_HIGHLIGHTS = [
    "Vape 4× Points (Smokers Warehouse SW1/SW2) is the clearest August win: loyalty rev +32% YoY, 68.3% share.",
    "Fireworks summer total $433k (+49% YoY) at SW1/SW2; August −56% is end-of-season clearance, not campaign failure.",
    "Twinleaf Grab N Go loyalty widened (cards +14.5%, trips +17.9%) but basket fell to $8.68 (−5.6%).",
    "Bagel+Coffee lives at Twinleaf TGC (12 confirmed combos); TXP needs a POS fix before measurement is reliable.",
]

CHAT_SUGGESTIONS = [
    "Summarize August results with metrics",
    "Which campaign performed best?",
    "Compare Twinleaf vs Smokers Warehouse",
    "What are the top recommendations?",
    "How did SW1 vs SW2 do on vape?",
    "FoodToGo store differences TXP vs TGC",
]


def campaign_by_id(campaign_id):
    return next((c for c in AUGUST_CAMPAIGNS if c["id"] == campaign_id), None)


def store_labels(store_keys):
    return [STORES[k]["short"] for k in store_keys if k in STORES]


def brand_for_stores(store_keys):
    brands = {STORES[k]["brand"] for k in store_keys if k in STORES}
    if len(brands) == 1:
        return next(iter(brands))
    if not brands:
        return "CAA"
    return "Twinleaf + Smokers Warehouse"


def reports_for_ui():
    """Shape used by templates and /api/reports."""
    out = []
    for c in AUGUST_CAMPAIGNS:
        out.append({
            **c,
            "store_labels": store_labels(c["stores"]),
            "store_count": len(c["stores"]),
        })
    return out


def metrics_brief(campaign, limit=4):
    parts = []
    for m in campaign.get("metrics", [])[:limit]:
        delta = f" ({m['delta']})" if m.get("delta") else ""
        parts.append(f"{m['label']} {m['value']}{delta}")
    return "; ".join(parts)


def full_knowledge_text():
    blocks = [
        "CAA August 2026 campaign facts (use these exact metrics; do not invent numbers).",
        "Brands: Smokers Warehouse = SW1 Akwesasne + SW2 Ft. Covington. Twinleaf = Twinleaf Express (TXP) + Twinleaf Gas & Convenience (TGC).",
    ]
    for c in AUGUST_CAMPAIGNS:
        stores = ", ".join(store_labels(c["stores"]))
        store_detail = "; ".join(
            f"{b['store']}: {b['detail']} ({b['delta']})" for b in c["store_breakdown"]
        )
        blocks.append(
            f"[{c['title']}] brand={c['brand']}; stores={stores}; status={c['status']}; offer={c['offer']}; "
            f"summary={c['summary']}; metrics={metrics_brief(c, 5)}; "
            f"store detail={store_detail}; "
            f"takeaway={c['takeaway']}; recommendation={c['recommendation']}"
        )
    blocks.append(
        "Recommendations: "
        + " | ".join(
            f"{r['title']} [{r['impact']}/{r['timing']}] ({r['brand']}): {r['detail']}"
            for r in RECOMMENDATIONS
        )
    )
    blocks.append("Key takeaways: " + " ".join(SUMMARY_HIGHLIGHTS))
    return "\n".join(blocks)


def executive_summary_answer():
    return (
        "August 2026: Vape 4× Points at Smokers Warehouse (SW1/SW2) is the clear win — "
        "total vape $100,279 (+3.6% YoY), loyalty $68,492 (+32%) at 68.3% share. "
        "Fireworks at SW1/SW2: August $5,806 (−56% YoY) is clearance; summer still $433k (+49%). "
        "Twinleaf Grab N Go (TXP/TGC): loyalty trips +18% but basket $8.68 (−5.6%). "
        "Bagel+Coffee (TXP/TGC): $1,667 bagel rev / 12 confirmed combos at TGC; fix TXP POS. "
        "Priority: re-run vape Q4, move fireworks to May–June, lift Grab N Go basket, fix TXP combo ringing."
    )


def match_campaigns(query: str):
    q = (query or "").lower()
    scored = []
    aliases = {
        "vape-loyalty": ["vape", "4x", "4×", "points on vape", "sw1", "sw2"],
        "fireworks": ["firework", "fw ", "seasonal", "clearance"],
        "foodtogoto": ["food", "grab", "gng", "foodtog", "food-to-go", "food to go"],
        "bagelcoffee": ["bagel", "coffee", "combo", "4.99"],
    }
    for c in AUGUST_CAMPAIGNS:
        score = 0
        if c["id"] in q or c["title"].lower() in q:
            score += 5
        for term in aliases.get(c["id"], []):
            if term in q:
                score += 2
        if c["brand"].lower() in q:
            score += 1
        for s in c["stores"]:
            if s.lower() in q or STORES[s]["location"].lower() in q:
                score += 2
        if "twinleaf" in q and c["brand"] == "Twinleaf":
            score += 2
        if ("smokers" in q or "warehouse" in q) and c["brand"] == "Smokers Warehouse":
            score += 2
        if score:
            scored.append((score, c))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [c for _, c in scored]


def answer_from_knowledge(query: str):
    """Deterministic, metric-grounded answers for common intents."""
    q = (query or "").lower().strip()
    matched = match_campaigns(q)

    wants_summary = any(t in q for t in ["summar", "overview", "at a glance", "results", "how did", "overall", "august"])
    wants_recs = any(t in q for t in ["recommend", "next step", "action", "should we", "priority", "q4"])
    wants_best = any(t in q for t in ["best", "strongest", "win", "top campaign", "perform"])
    wants_brand = "twinleaf" in q and ("smokers" in q or "warehouse" in q or "compare" in q or "vs" in q)
    wants_store = any(t in q for t in ["store", "sw1", "sw2", "txp", "tgc", "akwesasne", "covington", "express"])

    if wants_brand or ("compare" in q and ("brand" in q or "twinleaf" in q or "smokers" in q)):
        return (
            "Brand split is clean in August: Smokers Warehouse (SW1/SW2) ran Vape (+32% loyalty rev to $68.5k) "
            "and Fireworks (summer $433k). Twinleaf (TXP/TGC) ran Grab N Go (loyalty trips +18%, basket −5.6%) "
            "and Bagel+Coffee (TGC owns combos; TXP POS incomplete). "
            "SW is winning on loyalty category depth; Twinleaf needs basket lift + measurement fixes."
        ), matched or AUGUST_CAMPAIGNS, RECOMMENDATIONS[:3]

    if wants_best and not matched:
        c = campaign_by_id("vape-loyalty")
        return (
            f"Best August campaign: {c['title']} at {c['brand']} ({', '.join(store_labels(c['stores']))}). "
            f"{metrics_brief(c, 3)}. {c['takeaway']} Recommendation: {c['recommendation']}"
        ), [c], [RECOMMENDATIONS[0]]

    if wants_summary and not matched:
        return executive_summary_answer(), AUGUST_CAMPAIGNS, RECOMMENDATIONS[:3]

    if wants_recs and not matched:
        rec_text = "Top recommendations: " + " ".join(
            f"{i+1}) {r['title']} ({r['brand']} — {', '.join(r['stores'])}): {r['detail']}"
            for i, r in enumerate(RECOMMENDATIONS[:4])
        )
        return rec_text, AUGUST_CAMPAIGNS[:2], RECOMMENDATIONS[:4]

    if matched:
        c = matched[0]
        store_bits = "; ".join(f"{b['store']}: {b['detail']} ({b['delta']})" for b in c["store_breakdown"])
        answer = (
            f"{c['title']} — {c['brand']} stores {', '.join(store_labels(c['stores']))}. "
            f"Offer: {c['offer']}. {c['summary']} "
            f"Metrics: {metrics_brief(c, 4)}. "
        )
        if wants_store or len(matched) == 1:
            answer += f"By store: {store_bits}. "
        answer += f"Takeaway: {c['takeaway']} Next: {c['recommendation']}"
        recs = [r for r in RECOMMENDATIONS if c["id"].split("-")[0] in r["title"].lower() or c["brand"] in r["brand"] or any(s in r["stores"] for s in c["stores"])]
        return answer, matched[:2], (recs or RECOMMENDATIONS)[:3]

    if wants_recs:
        return answer_from_knowledge("recommendations")[0], AUGUST_CAMPAIGNS, RECOMMENDATIONS[:3]

    return executive_summary_answer(), AUGUST_CAMPAIGNS, RECOMMENDATIONS[:3]
