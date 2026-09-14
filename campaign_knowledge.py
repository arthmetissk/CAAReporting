"""Structured May–August 2026 campaign knowledge for dashboard + chat."""

STORES = {
    "SW1": {"name": "Smokers Warehouse 1", "short": "SW1 Akwesasne", "brand": "Smokers Warehouse", "location": "Akwesasne"},
    "SW2": {"name": "Smokers Warehouse 2", "short": "SW2 Ft. Covington", "brand": "Smokers Warehouse", "location": "Ft. Covington"},
    "TXP": {"name": "Twinleaf Express", "short": "TXP Express", "brand": "Twinleaf", "location": "Express / Ft. Covington"},
    "TGC": {"name": "Twinleaf Gas & Convenience", "short": "TGC Gas & Conv.", "brand": "Twinleaf", "location": "Akwesasne"},
}

BRANDS = {
    "Smokers Warehouse": ["SW1", "SW2"],
    "Twinleaf": ["TXP", "TGC"],
}

# ---------------------------------------------------------------------------
# Continuous / multi-month families
# ---------------------------------------------------------------------------
CAMPAIGN_FAMILIES = [
    {
        "id": "sandwich-deal",
        "name": "Sandwich Deal (Free Chip + Fountain)",
        "alias": ["sandwich", "free sandwich", "chip", "fountain", "$4.99 sandwich"],
        "brand": "Twinleaf",
        "stores": ["TGC", "TXP"],
        "months": ["May", "June", "July"],
        "offer": "$4.99 = sandwich + free 1oz chip + free 20oz fountain (saves $0.79–$0.99)",
        "summary": "Ongoing Twinleaf lunch loyalty mechanic May–July. TGC is the growth engine; TXP softer YoY but recovering MoM. Bundle POS completion stays very low (~0.5–1%).",
        "arc": [
            {"month": "May", "headline": "TGC +52% YoY baskets; TXP −32% YoY", "detail": "TGC 1,637 promo baskets; TXP 662. Bundle completion ~0.5–0.6%."},
            {"month": "June", "headline": "TGC +61% YoY; TXP recovering MoM", "detail": "TGC 1,882 baskets (+15% vs May); TXP −22% YoY but +9% MoM. Bundles 13/7."},
            {"month": "July", "headline": "Combined 1,916 baskets (−9.5% YoY, +1.8% MoM)", "detail": "Habitual loyalty buyers (TGC 85 cards / TXP 77). Only 11 full POS combos + 9 app redemptions."},
        ],
        "takeaway": "Sandwich buyers are high-repeat loyalty customers. Growth is in sandwich units, not detected free-chip/fountain completion — improve signage and POS ring discipline.",
        "recommendation": "Keep the deal; add visible in-store bundle cues and cashier prompts so free chip/fountain actually attach.",
        "campaign_ids": ["may-sandwich", "june-sandwich", "july-sandwich"],
    },
    {
        "id": "breakfast-coffee",
        "name": "Breakfast + Free Coffee Combo",
        "alias": ["coffee", "free coffee", "breakfast", "bfast", "$3.99"],
        "brand": "Twinleaf",
        "stores": ["TGC", "TXP"],
        "months": ["May", "June", "July", "August"],
        "offer": "$3.99 = breakfast sandwich + free coffee any size (saves $1.00–$1.70)",
        "summary": "Multi-month Twinleaf breakfast loop. TGC led explosive May–June growth; July normalized. August Bagel+Coffee is the related bundle evolution.",
        "arc": [
            {"month": "May", "headline": "TGC breakfast +114.5% YoY; combo rate 10.1%", "detail": "TXP combo rate 14.1% but breakfast −25% YoY. Free coffee fill tracked separately."},
            {"month": "June", "headline": "TGC still +103% YoY; combo 8.8%", "detail": "TXP −16% YoY breakfast, combo 11.6%. Strong continuity of the free-coffee mechanic."},
            {"month": "July", "headline": "1,380 breakfast baskets; 5.4% combo attach", "detail": "TGC +6.2% YoY / TXP +0.6%. $110.58 customer savings. Habitual return rates >92%."},
            {"month": "August", "headline": "Bagel+Coffee $4.99 snapshot (related bundle)", "detail": "334 bagels / 392 coffees; 12 confirmed same-basket combos at TGC only. TXP POS fix needed."},
        ],
        "takeaway": "Free coffee is a durable Twinleaf loyalty hook at TGC. Measurement quality depends on same-basket ringing — same issue recurs in August Bagel+Coffee at TXP.",
        "recommendation": "Protect the free-coffee mechanic at TGC; fix combo POS ringing at TXP before scaling Bagel+Coffee.",
        "campaign_ids": ["may-breakfast-coffee", "june-breakfast-coffee", "july-breakfast-coffee", "bagelcoffee"],
    },
    {
        "id": "fireworks",
        "name": "Fireworks Summer Program",
        "alias": ["firework", "fw", "seasonal", "spark"],
        "brand": "Smokers Warehouse",
        "stores": ["SW1", "SW2"],
        "months": ["May", "June", "July", "August"],
        "offer": "Tiered discounts (10/15/20%) early summer → clearance + 3× loyalty points in August",
        "summary": "Smokers Warehouse seasonal arc: May ramp → June peak (+17% YoY) → July Spark the 4th → August clearance (−56% YoY). Do not judge the program on August alone.",
        "arc": [
            {"month": "May", "headline": "Ramp month: revenue soft YoY, baskets larger", "detail": "SW1 FW −15% YoY rev / −36% baskets but +31% avg ticket. SW2 −20% rev, +60% avg ticket."},
            {"month": "June", "headline": "Peak: ~$150.7k FW (+16.6% YoY)", "detail": "Baskets −3.8% YoY but avg ticket +21%. Qualifying tier mix strong (~62–69%)."},
            {"month": "July", "headline": "Spark the 4th (Jun 23–Jul 6) 100% SW1 redemption", "detail": "15/15 qualifying baskets redeemed at SW1 — event mechanic worked."},
            {"month": "August", "headline": "Clearance: $5,806 (−55.7% YoY)", "detail": "Summer total still $433k (+49% YoY). SW1 −65% / SW2 −39% in August."},
        ],
        "takeaway": "Fireworks value is a summer story. June proves demand; August is inventory wind-down.",
        "recommendation": "Shift 2027 fireworks promotions to May–June (Memorial Day launch) with loyalty multiplier; keep August as clearance only.",
        "campaign_ids": ["may-fireworks", "june-fireworks", "july-spark-4th", "fireworks"],
    },
]

# ---------------------------------------------------------------------------
# Monthly executive stories (August-style)
# ---------------------------------------------------------------------------
MONTHLY_STORIES = [
    {
        "slug": "may",
        "month": "May 2026",
        "theme": "Loyalty foundations & trial",
        "filename": "2026_May_Main_Campaign_Performance_Summary.html",
        "brands": ["Twinleaf", "Smokers Warehouse"],
        "stores": ["TGC", "TXP", "SW1", "SW2"],
        "status": "Foundation",
        "summary": "May builds the loyalty base: Twinleaf sandwich + free-coffee loops, gas+pizza trial, Thunder ice cream proxy; Smokers Warehouse starts fireworks ramp and cigarillo activation.",
        "highlights": [
            "Sandwich deal (TGC/TXP): TGC promo baskets +52% YoY; TXP −32% YoY but +18% MoM.",
            "Breakfast + free coffee: TGC breakfast +114.5% YoY with 10.1% combo rate.",
            "Gas + free pizza slice (loyalty $30+): low redemption (TGC 0.5% / TXP 1.8%) — mechanic under-activated.",
            "Thunder Frolly ice cream: 124 units proxy signal; free barcode not in POS — tracking gap.",
            "Fireworks May ramp at SW1/SW2: softer revenue YoY but larger average tickets.",
        ],
        "metrics": [
            {"label": "Sandwich TGC baskets", "value": "1,637", "delta": "+52% YoY"},
            {"label": "Bfast TGC YoY", "value": "+114.5%", "delta": "10.1% combo rate"},
            {"label": "Frolly units", "value": "124", "delta": "TGC 70 · TXP 54"},
            {"label": "FW SW1 May", "value": "Soft YoY", "delta": "+31% avg ticket"},
        ],
        "recommendations": [
            "Fix Thunder free-ice-cream POS barcode so redemptions are measurable.",
            "Push gas+$30 pizza awareness — redemption rates are too low vs fill-up rates.",
            "Protect TGC sandwich and free-coffee momentum heading into June.",
        ],
        "campaign_ids": ["may-sandwich", "may-breakfast-coffee", "may-pizza-gas", "may-thunder", "may-fireworks", "may-cigarillos"],
    },
    {
        "slug": "june",
        "month": "June 2026",
        "theme": "Summer activation & scale",
        "filename": "2026_June_Main_Campaign_Performance_Summary.html",
        "brands": ["Twinleaf", "Smokers Warehouse"],
        "stores": ["TGC", "TXP", "SW1", "SW2"],
        "status": "Peak build",
        "summary": "June scales summer: Smart Water 2-for-$5 at Twinleaf, fireworks peak at Smokers Warehouse, and continuous sandwich / free-coffee loyalty loops keep running.",
        "highlights": [
            "Fireworks June peak: ~$150.7k combined (+16.6% YoY) with +21% average ticket.",
            "Smart Water 2-for-$5: 54% promo adoption; TXP reversed a 5-month adoption decline to 52%.",
            "Sandwich: TGC +61% YoY baskets; TXP still −22% YoY but +9% MoM.",
            "Breakfast + free coffee: TGC still +103% YoY; combo rates 8.8% / 11.6%.",
        ],
        "metrics": [
            {"label": "FW June rev", "value": "~$150.7k", "delta": "+16.6% YoY"},
            {"label": "Smart Water adoption", "value": "54%", "delta": "1,360 units"},
            {"label": "Sandwich TGC", "value": "1,882", "delta": "+61% YoY"},
            {"label": "TXP water units", "value": "+25.3%", "delta": "adoption 52%"},
        ],
        "recommendations": [
            "Treat June fireworks as the success benchmark for 2027 planning.",
            "Keep multi-buy water mechanics where TXP showed unmet demand.",
            "Continue sandwich MoM recovery focus at TXP.",
        ],
        "campaign_ids": ["june-sandwich", "june-breakfast-coffee", "june-fireworks", "june-smart-water"],
    },
    {
        "slug": "july",
        "month": "July 2026",
        "theme": "Summer acceleration",
        "filename": "2026_July_Promotions_Summary.html",
        "brands": ["Twinleaf", "Smokers Warehouse"],
        "stores": ["TGC", "TXP", "SW1", "SW2"],
        "status": "Active summer",
        "summary": "July mixes ongoing Twinleaf lunch/breakfast deals with Summer Cooler, Beat the Heat loyalty, ZYN buy-down at SW, and Spark the 4th fireworks event.",
        "highlights": [
            "Sandwich 1,916 trips (−9.5% YoY, +1.8% MoM); strong habitual loyalty return (>93%).",
            "Breakfast + free coffee: 1,380 baskets, 5.4% combo attach, $110.58 savings.",
            "Summer Cooler: qualifying 2-pack trips +8.9% YoY; 12.8% adoption; baskets +47% vs average beer buyer.",
            "ZYN stock-up: 1,338 units (+27.4% YoY, +14.8% MoM) at Smokers Warehouse.",
            "Spark the 4th: 100% redemption at SW1 (15/15).",
            "Beat the Heat: 236 loyalty cold-vault cards (+25.5% YoY), $18,494 loyalty revenue.",
        ],
        "metrics": [
            {"label": "Sandwich trips", "value": "1,916", "delta": "−9.5% YoY"},
            {"label": "ZYN units", "value": "1,338", "delta": "+27.4% YoY"},
            {"label": "Cooler qualify", "value": "+8.9%", "delta": "12.8% adoption"},
            {"label": "Spark 4th SW1", "value": "100%", "delta": "15/15 redeemed"},
        ],
        "recommendations": [
            "Lean into event mechanics like Spark the 4th that show perfect redemption.",
            "Use Cooler-style multi-buy to protect beer basket value even when volume softens.",
            "Pair lunch sandwich with clearer free side attach prompts.",
        ],
        "campaign_ids": ["july-sandwich", "july-breakfast-coffee", "july-cooler", "july-zyn", "july-spark-4th", "july-beat-heat"],
    },
    {
        "slug": "august",
        "month": "August 2026",
        "theme": "Optimization & learning",
        "filename": "2026_August_CAA_Campaign_Summary.html",
        "brands": ["Twinleaf", "Smokers Warehouse"],
        "stores": ["TGC", "TXP", "SW1", "SW2"],
        "status": "Strongest readout",
        "summary": "August splits cleanly: Smokers Warehouse wins on Vape 4× Points; Fireworks is clearance; Twinleaf Grab N Go widens loyalty but basket thins; Bagel+Coffee needs POS fix at TXP.",
        "highlights": [
            "Vape 4× Points: $100,279 total (+3.6%), loyalty $68,492 (+32%), 68.3% share — clearest win.",
            "Fireworks August $5,806 (−56%) but summer $433k (+49%) — wrong month to judge.",
            "Grab N Go: cards +14.5%, trips +17.9%, basket $8.68 (−5.6%).",
            "Bagel+Coffee: 334 bagels / 12 combos at TGC; TXP rings items separately.",
        ],
        "metrics": [
            {"label": "Vape total", "value": "$100,279", "delta": "loyalty +32%"},
            {"label": "Summer FW", "value": "$433,069", "delta": "+49% YoY"},
            {"label": "Grab N Go", "value": "$109,603", "delta": "basket −5.6%"},
            {"label": "Bagel rev", "value": "$1,667", "delta": "12 combos TGC"},
        ],
        "recommendations": [
            "Re-run Vape 4× in Q4 at SW1/SW2.",
            "Move fireworks promo weight to May–June 2027.",
            "Add Grab N Go bundle to lift basket; fix TXP Bagel+Coffee POS.",
        ],
        "campaign_ids": ["vape-loyalty", "fireworks", "foodtogoto", "bagelcoffee"],
    },
]

# ---------------------------------------------------------------------------
# Individual campaigns
# ---------------------------------------------------------------------------
def _c(**kwargs):
    return kwargs


CAMPAIGNS = [
    # May
    _c(id="may-sandwich", family="sandwich-deal", month="May", month_slug="may", filename="2026_May_37_Sandwich_Deal_Loyalty_Promo_Twinleaf.html",
       title="Sandwich Deal — May", category="Ongoing loyalty", status="Strong@TGC", signal=78,
       brand="Twinleaf", stores=["TGC", "TXP"], offer="$4.99 sandwich + free chip + free fountain", period="May 1–31, 2026",
       summary="TGC promo sandwich baskets +52% YoY; TXP −32% YoY but +18% MoM.",
       metrics=[{"label": "TGC baskets", "value": "1,637", "delta": "+52% YoY"}, {"label": "TXP baskets", "value": "662", "delta": "−32% YoY"},
                {"label": "TGC revenue", "value": "+58% YoY", "delta": "promo sand."}, {"label": "Bundle complete", "value": "~0.6%", "delta": "TGC 10 · TXP 3"}],
       store_breakdown=[{"store": "TGC", "detail": "1,637 promo baskets · +59% units · +58% rev", "delta": "+52% YoY"},
                        {"store": "TXP", "detail": "662 promo baskets · −31% rev · +18% MoM", "delta": "−32% YoY"}],
       takeaway="TGC is the sandwich growth store; free chip/fountain almost never attach in POS.",
       recommendation="Keep funding TGC sandwich; coach TXP recovery and bundle ringing."),
    _c(id="may-breakfast-coffee", family="breakfast-coffee", month="May", month_slug="may", filename="2026_May_38_Breakfast_Coffee_Combo_Loyalty_Promo_Twinleaf.html",
       title="Breakfast + Free Coffee — May", category="Ongoing loyalty", status="Strong@TGC", signal=85,
       brand="Twinleaf", stores=["TGC", "TXP"], offer="$3.99 breakfast sandwich + free coffee", period="May 1–31, 2026",
       summary="TGC breakfast +114.5% YoY with 10.1% combo rate; TXP higher combo rate (14.1%) but softer breakfast YoY.",
       metrics=[{"label": "TGC bfast YoY", "value": "+114.5%", "delta": "1,298 baskets"}, {"label": "TGC combo", "value": "10.1%", "delta": "bfast+coffee"},
                {"label": "TXP combo", "value": "14.1%", "delta": "bfast −25% YoY"}, {"label": "TGC bfast rev", "value": "+145% YoY", "delta": "coffee units +140%"}],
       store_breakdown=[{"store": "TGC", "detail": "1,298 breakfast baskets · 10.1% combo", "delta": "+114.5% YoY"},
                        {"store": "TXP", "detail": "combo 14.1% · breakfast −25% YoY", "delta": "coffee +52% YoY"}],
       takeaway="Free coffee is working as a Twinleaf habit builder, especially at TGC.",
       recommendation="Scale free-coffee messaging at TGC; diagnose TXP breakfast softness."),
    _c(id="may-pizza-gas", family="one-off", month="May", month_slug="may", filename="2026_May_39_Pizza_Gas_Loyalty_Twinleaf.html",
       title="Gas $30 + Free Pizza Slice — May", category="Loyalty trial", status="Underused", signal=55,
       brand="Twinleaf", stores=["TGC", "TXP"], offer="Loyalty: $30+ gas fill → free pizza slice ($3.25)", period="May 1–31, 2026",
       summary="Loyalty customers already hit $30+ gas often, but pizza redemptions are tiny (TGC 0.5% / TXP 1.8%).",
       metrics=[{"label": "TGC redeem rate", "value": "0.5%", "delta": "of loyalty $30+ fills"}, {"label": "TXP redeem rate", "value": "1.8%", "delta": "3.6× TGC"},
                {"label": "TGC $30+ loyalty", "value": "84.8%", "delta": "of loyalty fills"}, {"label": "TXP $30+ loyalty", "value": "85.7%", "delta": "of loyalty fills"}],
       store_breakdown=[{"store": "TGC", "detail": "High $30+ loyalty fills, almost no pizza claims", "delta": "0.5% redeem"},
                        {"store": "TXP", "detail": "Still low but 3.6× TGC redemption", "delta": "1.8% redeem"}],
       takeaway="Offer awareness/ops gap — eligibility is high, claims are not.",
       recommendation="Add pump/POS prompts for free pizza when loyalty gas ≥ $30."),
    _c(id="may-thunder", family="one-off", month="May", month_slug="may", filename="2026_May_34_Thunder_Ice_Cream_Campaign_Twinleaf.html",
       title="Thunder Free Frolly Ice Cream — May", category="Seasonal trial", status="Tracking gap", signal=50,
       brand="Twinleaf", stores=["TGC", "TXP"], offer="Free Frolly after Akwesasne Thunder win (day-after)", period="May 2026",
       summary="124 Frolly units as proxy signal; free redemption barcode not in POS so paid vs free cannot be separated.",
       metrics=[{"label": "Frolly units", "value": "124", "delta": "TGC 70 · TXP 54"}, {"label": "Est. incr. rev", "value": "$1,273", "delta": "ex-item cost"},
                {"label": "TXP YoY units", "value": "+64%", "delta": "vs 33 in 2025"}, {"label": "Free barcode", "value": "Missing", "delta": "POS setup needed"}],
       store_breakdown=[{"store": "TGC", "detail": "70 units in 59 baskets · avg basket $14.50", "delta": "new vs 2025"},
                        {"store": "TXP", "detail": "54 units · avg basket $17.00 · +64% YoY", "delta": "proxy only"}],
       takeaway="Campaign interest exists, but measurement is broken without the free SKU.",
       recommendation="Load Thunder free barcode into POS before next season."),
    _c(id="may-fireworks", family="fireworks", month="May", month_slug="may", filename="2026_May_35_Fireworks_Promo_Smokers_Warehouse.html",
       title="Fireworks Promo — May", category="Seasonal ramp", status="Ramp", signal=60,
       brand="Smokers Warehouse", stores=["SW1", "SW2"], offer="Tiered FW discounts 10/15/20%", period="May 1–31, 2026",
       summary="May ramp: revenue soft YoY but average fireworks tickets up sharply — customers spending into tiers.",
       metrics=[{"label": "SW1 FW rev", "value": "−15% YoY", "delta": "avg ticket +31%"}, {"label": "SW2 FW rev", "value": "−20% YoY", "delta": "avg ticket +60%"},
                {"label": "SW1 loyalty FW", "value": "36.8%", "delta": "was 23.7%"}, {"label": "SW2 baskets", "value": "−50% YoY", "delta": "larger tickets"}],
       store_breakdown=[{"store": "SW1", "detail": "Softer rev/baskets, higher loyalty coverage", "delta": "−15% rev"},
                        {"store": "SW2", "detail": "Fewer baskets, much larger average ticket", "delta": "−20% rev"}],
       takeaway="May is setup month — judge fireworks on June/July peak.",
       recommendation="Use May for awareness + tier education, not peak ROI readout."),
    _c(id="may-cigarillos", family="one-off", month="May", month_slug="may", filename="2026_May_36_Game_Cigarillos_Promo_Smokers_Warehouse.html",
       title="Game Cigarillos Promo — May", category="Category activation", status="Activation", signal=58,
       brand="Smokers Warehouse", stores=["SW1", "SW2"], offer="Game cigarillos promotional activation", period="May 2026",
       summary="Smokers Warehouse category activation alongside early fireworks season.",
       metrics=[{"label": "Brand", "value": "SW", "delta": "SW1 + SW2"}, {"label": "Type", "value": "One-off", "delta": "May activation"}],
       store_breakdown=[{"store": "SW1", "detail": "Included in May SW promo set", "delta": "Akwesasne"},
                        {"store": "SW2", "detail": "Included in May SW promo set", "delta": "Ft. Covington"}],
       takeaway="Supports May SW traffic mix; not a multi-month family.",
       recommendation="Review only if category margin supports repeat."),

    # June
    _c(id="june-sandwich", family="sandwich-deal", month="June", month_slug="june", filename="2026_June_37_Sandwich_Deal_Loyalty_Promo_Twinleaf.html",
       title="Sandwich Deal — June", category="Ongoing loyalty", status="Strong@TGC", signal=80,
       brand="Twinleaf", stores=["TGC", "TXP"], offer="$4.99 sandwich + free chip + free fountain", period="June 1–30, 2026",
       summary="TGC continues acceleration (+61% YoY, +15% MoM). TXP still down YoY but recovering vs May.",
       metrics=[{"label": "TGC baskets", "value": "1,882", "delta": "+61% YoY"}, {"label": "TXP baskets", "value": "−22% YoY", "delta": "+9% MoM"},
                {"label": "TGC rev", "value": "+60% YoY", "delta": "promo sand."}, {"label": "Bundles", "value": "20", "delta": "TGC 13 · TXP 7"}],
       store_breakdown=[{"store": "TGC", "detail": "1,882 baskets · 0.7% bundle completion", "delta": "+61% YoY"},
                        {"store": "TXP", "detail": "MoM recovery +9.2% · 1.0% bundle rate", "delta": "−22% YoY"}],
       takeaway="Family continuity is real at TGC; TXP needs continued MoM attention.",
       recommendation="Keep sandwich as a continuous Twinleaf family through summer."),
    _c(id="june-breakfast-coffee", family="breakfast-coffee", month="June", month_slug="june", filename="2026_June_38_Breakfast_Coffee_Combo_Loyalty_Promo_Twinleaf.html",
       title="Breakfast + Free Coffee — June", category="Ongoing loyalty", status="Strong@TGC", signal=82,
       brand="Twinleaf", stores=["TGC", "TXP"], offer="$3.99 breakfast + free coffee", period="June 1–30, 2026",
       summary="TGC breakfast still +103% YoY; combo rates 8.8% TGC / 11.6% TXP.",
       metrics=[{"label": "TGC bfast YoY", "value": "+103%", "delta": "1,436 baskets"}, {"label": "TGC combo", "value": "8.8%", "delta": "+10.6% MoM baskets"},
                {"label": "TXP combo", "value": "11.6%", "delta": "bfast −16% YoY"}, {"label": "TGC coffee", "value": "+124% YoY", "delta": "units"}],
       store_breakdown=[{"store": "TGC", "detail": "1,436 baskets · free coffee still attaching", "delta": "+103% YoY"},
                        {"store": "TXP", "detail": "Higher combo %, softer breakfast base", "delta": "−16% YoY"}],
       takeaway="Free-coffee family remains a Twinleaf continuity asset.",
       recommendation="Maintain offer; watch TXP breakfast base."),
    _c(id="june-fireworks", family="fireworks", month="June", month_slug="june", filename="2026_June_41_Fireworks_June_2026_Campaign_Performance.html",
       title="Fireworks — June Peak", category="Seasonal peak", status="Strong", signal=88,
       brand="Smokers Warehouse", stores=["SW1", "SW2"], offer="Tiered FW discounts 10/15/20%", period="June 1–30, 2026",
       summary="Peak summer fireworks: ~$150.7k (+16.6% YoY). Fewer baskets but much larger tickets.",
       metrics=[{"label": "FW revenue", "value": "~$150.7k", "delta": "+16.6% YoY"}, {"label": "Baskets", "value": "−3.8% YoY", "delta": "avg ticket +21%"},
                {"label": "SW1 rev", "value": "+15.7%", "delta": "YoY"}, {"label": "SW2 rev", "value": "+16.7%", "delta": "YoY"}],
       store_breakdown=[{"store": "SW1", "detail": "Strong YoY revenue with solid qualifying mix", "delta": "+15.7%"},
                        {"store": "SW2", "detail": "Similar strength; ticket growth key", "delta": "+16.7%"}],
       takeaway="June is the fireworks success month — use it as the planning anchor.",
       recommendation="Budget 2027 fireworks around June peak, not August."),
    _c(id="june-smart-water", family="one-off", month="June", month_slug="june", filename="2026_June_44_Smart_Water_2for5_Campaign_Performance.html",
       title="Smart Water 2-for-$5 — June", category="Trade promo", status="Effective@TXP", signal=75,
       brand="Twinleaf", stores=["TGC", "TXP"], offer="2× 1L Smart Water for $5 (all customers)", period="June 2026",
       summary="54% adoption combined. TXP reversed a long adoption decline to 52% and grew units +25% YoY.",
       metrics=[{"label": "Units", "value": "1,360", "delta": "−3.3% YoY"}, {"label": "Adoption", "value": "54%", "delta": "avg 1.61 units/txn"},
                {"label": "TXP units", "value": "+25.3%", "delta": "adoption 52%"}, {"label": "TGC units", "value": "−13.9%", "delta": "adoption 55%"}],
       store_breakdown=[{"store": "TGC", "detail": "885 units · adoption 55% (+11.5pp YoY)", "delta": "−14% units"},
                        {"store": "TXP", "detail": "475 units · adoption recovered to 52%", "delta": "+25% units"}],
       takeaway="Multi-buy works — especially where unmet demand existed at TXP.",
       recommendation="Reuse 2-for mechanics at TXP on similar beverage sets."),

    # July
    _c(id="july-sandwich", family="sandwich-deal", month="July", month_slug="july", filename="2026_July_37d_Sandwich_Deal_Loyalty_Promo_Twinleaf.html",
       title="Sandwich Deal — July", category="Ongoing loyalty", status="Habitual", signal=70,
       brand="Twinleaf", stores=["TGC", "TXP"], offer="$4.99 sandwich + free chip + free fountain", period="July 1–31, 2026",
       summary="1,916 sandwich trips (−9.5% YoY, +1.8% MoM). Loyalty buyers are habitual (>93% return).",
       metrics=[{"label": "Sandwich trips", "value": "1,916", "delta": "−9.5% YoY"}, {"label": "Full combos", "value": "11", "delta": "POS detected"},
                {"label": "App redeems", "value": "9", "delta": "Patron Points"}, {"label": "TGC cards", "value": "85", "delta": "83.5% multi-month"}],
       store_breakdown=[{"store": "TGC", "detail": "1,222 trips (−1.4% YoY) · 85 cards · 6 POS combos", "delta": "stable"},
                        {"store": "TXP", "detail": "694 trips (−20.9% YoY) · 77 cards · 5 POS combos", "delta": "softer"}],
       takeaway="Continuity > promo spike: sandwich is a loyalty habit loop with weak free-side attach.",
       recommendation="Improve free chip/fountain attach with signage + cashier prompts."),
    _c(id="july-breakfast-coffee", family="breakfast-coffee", month="July", month_slug="july", filename="2026_July_38d_Breakfast_Coffee_Combo_Loyalty_Promo_Twinleaf.html",
       title="Breakfast + Free Coffee — July", category="Ongoing loyalty", status="Steady", signal=72,
       brand="Twinleaf", stores=["TGC", "TXP"], offer="$3.99 breakfast + free coffee", period="July 1–31, 2026",
       summary="1,380 breakfast baskets; 5.4% combo attach; $110.58 savings. Return rates remain excellent.",
       metrics=[{"label": "Bfast baskets", "value": "1,380", "delta": "TGC 715 · TXP 665"}, {"label": "Combo attach", "value": "5.4%", "delta": "TGC 7.0% · TXP 3.6%"},
                {"label": "Savings", "value": "$110.58", "delta": "avg $1.49/combo"}, {"label": "PP redeems", "value": "18", "delta": "TGC 15 · TXP 3"}],
       store_breakdown=[{"store": "TGC", "detail": "+6.2% YoY baskets · 7.0% combo · 96.4% return", "delta": "strong habit"},
                        {"store": "TXP", "detail": "+0.6% YoY · 3.6% combo · 92.6% return", "delta": "steady"}],
       takeaway="Free coffee remains a sticky Twinleaf morning loop.",
       recommendation="Keep offer; migrate learnings into August Bagel+Coffee with better POS."),
    _c(id="july-cooler", family="one-off", month="July", month_slug="july", filename="2026_July_45_Summer_Cooler_Deal.html",
       title="Summer Cooler Deal — July", category="Seasonal deal", status="Effective", signal=76,
       brand="Twinleaf", stores=["TGC", "TXP"], offer="Buy 2 beer 12-packs, get free bag of ice", period="July 2026",
       summary="Qualifying 2-pack trips +8.9% YoY; 12.8% adoption; those trips spend ~47% more than average beer buyers.",
       metrics=[{"label": "Qualify trips", "value": "+8.9% YoY", "delta": "2-pack behavior"}, {"label": "Adoption", "value": "12.8%", "delta": "was 11.4%"},
                {"label": "Beer units", "value": "−3.1% YoY", "delta": "after strong June"}, {"label": "Basket vs avg", "value": "+47%", "delta": "qualifiers"}],
       store_breakdown=[{"store": "TGC", "detail": "Participating Twinleaf cooler stores", "delta": "multi-buy"},
                        {"store": "TXP", "detail": "Participating Twinleaf cooler stores", "delta": "multi-buy"}],
       takeaway="Deal improved trip quality even when total beer units softened.",
       recommendation="Reuse free-ice / multi-buy framing for summer beer occasions."),
    _c(id="july-zyn", family="one-off", month="July", month_slug="july", filename="2026_July_46_ZYN_BuyDown_SW.html",
       title="ZYN Stock-Up BuyDown — July", category="Category activation", status="Strong", signal=84,
       brand="Smokers Warehouse", stores=["SW1", "SW2"], offer="ZYN stock-up discount", period="July 2026",
       summary="1,338 ZYN units (+27.4% YoY, +14.8% MoM) — clear SW category win.",
       metrics=[{"label": "Units", "value": "1,338", "delta": "+27.4% YoY"}, {"label": "MoM", "value": "+14.8%", "delta": "vs June"},
                {"label": "Brand", "value": "SW", "delta": "SW1 + SW2"}],
       store_breakdown=[{"store": "SW1", "detail": "Included in SW ZYN buy-down", "delta": "+YoY"},
                        {"store": "SW2", "detail": "Included in SW ZYN buy-down", "delta": "+YoY"}],
       takeaway="Category buy-downs can still deliver hard unit growth at SW.",
       recommendation="Keep ZYN-style stock-up events on the SW calendar."),
    _c(id="july-spark-4th", family="fireworks", month="July", month_slug="july", filename="2026_June_July_41e_Spark_the_4th.html",
       title="Spark the 4th — Jul event", category="Event", status="Perfect redeem", signal=90,
       brand="Smokers Warehouse", stores=["SW1"], offer="Spark the 4th fireworks event (Jun 23–Jul 6)", period="Jun 23–Jul 6, 2026",
       summary="100% redemption at SW1 — 15 of 15 qualifying baskets redeemed.",
       metrics=[{"label": "Redemption", "value": "100%", "delta": "SW1"}, {"label": "Qualifying", "value": "15/15", "delta": "baskets"},
                {"label": "Window", "value": "Jun23–Jul6", "delta": "event"}],
       store_breakdown=[{"store": "SW1", "detail": "15/15 qualifying baskets redeemed", "delta": "100%"},
                        {"store": "SW2", "detail": "Event reporting focused on SW1", "delta": "see report"}],
       takeaway="Short event mechanics can outperform long vague promos.",
       recommendation="Clone Spark-style event design for 2027 holiday windows."),
    _c(id="july-beat-heat", family="one-off", month="July", month_slug="july", filename="2026_July_47a_BeatHeat_Loyalty.html",
       title="Members Beat the Heat — July", category="Loyalty", status="Growing", signal=77,
       brand="Twinleaf + Smokers Warehouse", stores=["TGC", "TXP", "SW1", "SW2"], offer="Loyalty cold-vault / beat-the-heat member offer", period="July 2026",
       summary="236 loyalty cold-vault cards (+25.5% YoY) and $18,494 loyalty revenue across the heat offer.",
       metrics=[{"label": "Loyalty cards", "value": "236", "delta": "+25.5% YoY"}, {"label": "Loyalty rev", "value": "$18,494", "delta": "cold vault"},
                {"label": "Scope", "value": "All 4 stores", "delta": "heat occasion"}],
       store_breakdown=[{"store": "TGC", "detail": "Included in all-store loyalty heat program", "delta": "Twinleaf"},
                        {"store": "TXP", "detail": "Included in all-store loyalty heat program", "delta": "Twinleaf"},
                        {"store": "SW1", "detail": "Included in all-store loyalty heat program", "delta": "SW"},
                        {"store": "SW2", "detail": "Included in all-store loyalty heat program", "delta": "SW"}],
       takeaway="Cross-banner loyalty occasion offers can grow card engagement in summer.",
       recommendation="Reuse heat/occasion loyalty framing next summer."),

    # August (existing detailed set)
    _c(id="vape-loyalty", family="one-off", month="August", month_slug="august", filename="2026_August_41g_Vape_Loyalty_Campaign.html",
       title="Vape Loyalty Campaign", category="Loyalty & retention", status="Strong", signal=90,
       brand="Smokers Warehouse", stores=["SW1", "SW2"], offer="4× points on all vape purchases (loyalty only)", period="August 1–31, 2026",
       summary="Clearest August win: loyalty vape revenue +32% YoY while non-loyalty fell −29%.",
       metrics=[{"label": "Total vape rev", "value": "$100,279", "delta": "+3.6% YoY"}, {"label": "Loyalty rev", "value": "$68,492", "delta": "+32.0% YoY"},
                {"label": "Loyalty share", "value": "68.3%", "delta": "144 cards · 1,420 trips"}, {"label": "Non-loyalty rev", "value": "$31,787", "delta": "−29.2% YoY"},
                {"label": "Summer vape", "value": "$377,809", "delta": "+14.0% YoY"}],
       store_breakdown=[{"store": "SW1", "detail": "$66,654 total · $45,365 loyalty · 82 cards · 927 trips", "delta": "+3.4%"},
                        {"store": "SW2", "detail": "$33,625 total · $23,126 loyalty · 62 cards · 493 trips", "delta": "+4.1%"}],
       takeaway="SW1 drives ~66% of combined vape; SW2 grew slightly faster.",
       recommendation="Re-run Vape 4× Points in Q4, ideally tied to a new SKU or seasonal brand push."),
    _c(id="fireworks", family="fireworks", month="August", month_slug="august", filename="2026_August_41f_Fireworks_Campaign.html",
       title="Fireworks Campaign — August", category="Seasonal clearance", status="Context", signal=72,
       brand="Smokers Warehouse", stores=["SW1", "SW2"], offer="20% off remaining inventory + 3× points on fireworks", period="August 1–31, 2026",
       summary="August is clearance, not peak: Aug FW −55.7% YoY, but summer FW +49% YoY to $433k.",
       metrics=[{"label": "Aug FW rev", "value": "$5,806", "delta": "−55.7% YoY"}, {"label": "Summer FW", "value": "$433,069", "delta": "+49.0% YoY"},
                {"label": "Loyalty rev", "value": "$405", "delta": "7.0% share · 13 cards"}, {"label": "FW baskets", "value": "92", "delta": "vs 128 Aug 2025"}],
       store_breakdown=[{"store": "SW1", "detail": "$2,924 · 52 baskets · loyalty $168 (6 cards)", "delta": "−65.0%"},
                        {"store": "SW2", "detail": "$2,882 · 40 baskets · loyalty $237 (7 cards)", "delta": "−39.4%"}],
       takeaway="SW1’s August drop nearly double SW2’s; summer peak was June/July.",
       recommendation="Shift fireworks promotions to May–June 2027 with a Memorial Day loyalty multiplier."),
    _c(id="foodtogoto", family="one-off", month="August", month_slug="august", filename="2026_August_41h_FoodToGo_Loyalty_Campaign.html",
       title="FoodToGo / Grab N Go Loyalty", category="On-the-go food", status="Mixed", signal=74,
       brand="Twinleaf", stores=["TXP", "TGC"], offer="2× points on any Grab N Go purchase (loyalty only)", period="August 1–31, 2026",
       summary="Loyalty cards/trips up, but total Grab N Go −4.6% and avg basket −5.6%.",
       metrics=[{"label": "Total Grab N Go", "value": "$109,603", "delta": "−4.6% YoY"}, {"label": "Loyalty rev", "value": "$12,641", "delta": "+11.3% YoY"},
                {"label": "Loyalty cards", "value": "142", "delta": "+14.5% · 1,456 trips"}, {"label": "Avg basket/trip", "value": "$8.68", "delta": "−5.6% YoY"}],
       store_breakdown=[{"store": "TXP", "detail": "72 cards · 886 trips (+32.4%) · $9.60 basket (−10.9%)", "delta": "frequency up"},
                        {"store": "TGC", "detail": "70 cards · 570 trips (+0.7%) · $7.26 basket (−0.8%)", "delta": "basket steady"}],
       takeaway="Opposite store responses; no new Grab N Go loyalty enrollments.",
       recommendation="Add a Grab N Go bundle mechanic to lift avg basket; launch POS enrollment prompts."),
    _c(id="bagelcoffee", family="breakfast-coffee", month="August", month_slug="august", filename="2026_August_41i_BagelCoffeeCombo_Snapshot.html",
       title="Bagel Coffee Combo Snapshot", category="Bundle snapshot", status="Baseline", signal=64,
       brand="Twinleaf", stores=["TXP", "TGC"], offer="Bagel + Coffee for $4.99 (all customers)", period="August 1–31, 2026",
       summary="First tracked month: 334 bagels ($1,667) and 392 coffees ($526). TGC is the combo home.",
       metrics=[{"label": "Bagel units", "value": "334", "delta": "$1,667 rev"}, {"label": "Coffee units", "value": "392", "delta": "$526 rev"},
                {"label": "Same-basket combos", "value": "12", "delta": "TGC only"}, {"label": "Non-loyalty share", "value": "~83%", "delta": "of purchases"}],
       store_breakdown=[{"store": "TXP", "detail": "150 bagels ($749) · 69 coffees ($79) · 0 same-basket combos", "delta": "POS fix needed"},
                        {"store": "TGC", "detail": "184 bagels ($918) · 323 coffees ($447) · 12 confirmed combos", "delta": "natural home"}],
       takeaway="Extension of free-coffee family; TXP measurement blocked by separate ringing.",
       recommendation="Fix TXP POS combo ringing; treat September as Month 1 clean baseline."),
]

AUGUST_CAMPAIGNS = [c for c in CAMPAIGNS if c["month"] == "August"]

RECOMMENDATIONS = [
    {"title": "Re-run Vape 4× Points in Q4", "impact": "High", "timing": "Q4 Action", "stores": ["SW1", "SW2"], "brand": "Smokers Warehouse",
     "detail": "Highest-ROI August structure. Loyalty vape +32% YoY at 68.3% share."},
    {"title": "Plan fireworks around May–June peak", "impact": "High", "timing": "2027 Plan", "stores": ["SW1", "SW2"], "brand": "Smokers Warehouse",
     "detail": "June ~$151k (+17% YoY) and summer $433k (+49%). August is clearance only."},
    {"title": "Protect Twinleaf free-coffee & sandwich families", "impact": "High", "timing": "Ongoing", "stores": ["TGC", "TXP"], "brand": "Twinleaf",
     "detail": "Multi-month continuity at TGC. Improve free side/coffee attach with POS + signage."},
    {"title": "Fix combo POS ringing at TXP", "impact": "Medium", "timing": "Ops Fix", "stores": ["TXP"], "brand": "Twinleaf",
     "detail": "Breakfast/coffee and Bagel+Coffee both need same-basket ringing for measurement."},
    {"title": "Lift Grab N Go basket with bundles", "impact": "Medium", "timing": "Q4 Action", "stores": ["TXP", "TGC"], "brand": "Twinleaf",
     "detail": "Trips up, basket $8.68 (−5.6%). Pair with breakfast/bagel mechanics."},
]

SUMMARY_HIGHLIGHTS = [
    "Continuous Twinleaf families: Sandwich (free chip/fountain) and Breakfast+Free Coffee run May–July; Bagel+Coffee continues the coffee story in August.",
    "Fireworks is a Smokers Warehouse multi-month arc: May ramp → June peak → July Spark event → August clearance.",
    "August’s clearest single-month win is Vape 4× Points at SW1/SW2 (loyalty +32% YoY).",
    "Browse by month, store, campaign, or continuous family to see the same metrics in the right lens.",
]

CHAT_SUGGESTIONS = [
    "Summarize May like the August story",
    "Summarize June results with metrics",
    "Summarize July promotions",
    "Show the free coffee family across months",
    "Show sandwich deal May–July",
    "Fireworks story May–August",
    "What happened at SW1?",
    "Compare TGC vs TXP sandwich",
    "Campaigns at Twinleaf only",
]


def store_labels(store_keys):
    return [STORES[k]["short"] for k in store_keys if k in STORES]


def campaign_by_id(campaign_id):
    return next((c for c in CAMPAIGNS if c["id"] == campaign_id), None)


def family_by_id(family_id):
    return next((f for f in CAMPAIGN_FAMILIES if f["id"] == family_id), None)


def month_by_slug(slug):
    return next((m for m in MONTHLY_STORIES if m["slug"] == slug), None)


def enrich_campaign(c):
    return {**c, "store_labels": store_labels(c["stores"]), "store_count": len(c["stores"])}


def reports_for_ui():
    return [enrich_campaign(c) for c in AUGUST_CAMPAIGNS]


def all_campaigns_for_ui():
    return [enrich_campaign(c) for c in CAMPAIGNS]


def families_for_ui():
    out = []
    for f in CAMPAIGN_FAMILIES:
        linked = [enrich_campaign(campaign_by_id(cid)) for cid in f["campaign_ids"] if campaign_by_id(cid)]
        out.append({**f, "store_labels": store_labels(f["stores"]), "campaigns": linked})
    return out


def months_for_ui():
    out = []
    for m in MONTHLY_STORIES:
        linked = [enrich_campaign(campaign_by_id(cid)) for cid in m["campaign_ids"] if campaign_by_id(cid)]
        out.append({**m, "store_labels": store_labels(m["stores"]), "campaigns": linked})
    return out


def metrics_brief(campaign, limit=4):
    parts = []
    for m in campaign.get("metrics", [])[:limit]:
        delta = f" ({m['delta']})" if m.get("delta") else ""
        parts.append(f"{m['label']} {m['value']}{delta}")
    return "; ".join(parts)


def full_knowledge_text():
    blocks = [
        "CAA May–August 2026 campaign facts. Brands: Smokers Warehouse=SW1/SW2; Twinleaf=TXP/TGC. Use exact metrics only.",
        "Continuous families: " + " || ".join(
            f"{f['name']} ({', '.join(f['months'])}) stores={', '.join(f['stores'])}: {f['summary']}"
            for f in CAMPAIGN_FAMILIES
        ),
    ]
    for m in MONTHLY_STORIES:
        blocks.append(
            f"MONTH {m['month']}: theme={m['theme']}; summary={m['summary']}; "
            f"highlights={'; '.join(m['highlights'])}; metrics={'; '.join(x['label']+': '+x['value']+' '+x['delta'] for x in m['metrics'])}; "
            f"recs={'; '.join(m['recommendations'])}"
        )
    for c in CAMPAIGNS:
        store_detail = "; ".join(f"{b['store']}: {b['detail']} ({b['delta']})" for b in c["store_breakdown"])
        blocks.append(
            f"[{c['id']}] {c['title']} month={c['month']} brand={c['brand']} stores={', '.join(c['stores'])} "
            f"family={c.get('family')}: {c['summary']} metrics={metrics_brief(c, 5)}; stores={store_detail}; "
            f"takeaway={c['takeaway']}; next={c['recommendation']}"
        )
    blocks.append("Portfolio recommendations: " + " | ".join(f"{r['title']}: {r['detail']}" for r in RECOMMENDATIONS))
    return "\n".join(blocks)


def executive_summary_answer():
    return (
        "May–August 2026 story: Twinleaf continuous families are Sandwich (free chip/fountain) and Breakfast+Free Coffee — "
        "TGC leads growth, TXP needs attach/POS discipline. Smokers Warehouse fireworks arc peaks in June (~$151k, +17% YoY) "
        "and should not be judged on August clearance. August’s best single campaign is Vape 4× Points at SW1/SW2 "
        "(loyalty +32% to $68.5k). Browse by month, store, campaign, or family for the detailed metrics."
    )


def match_families(query: str):
    q = (query or "").lower()
    hits = []
    for f in CAMPAIGN_FAMILIES:
        score = 0
        if f["id"] in q or f["name"].lower() in q:
            score += 5
        for a in f.get("alias", []):
            if a in q:
                score += 3
        if score:
            hits.append((score, f))
    hits.sort(key=lambda x: x[0], reverse=True)
    return [f for _, f in hits]


def match_months(query: str):
    q = (query or "").lower()
    hits = []
    for m in MONTHLY_STORIES:
        if m["slug"] in q or m["month"].split()[0].lower() in q:
            hits.append(m)
    return hits


def match_campaigns(query: str):
    q = (query or "").lower()
    scored = []
    for c in CAMPAIGNS:
        score = 0
        if c["id"] in q or c["title"].lower() in q:
            score += 5
        if c["month"].lower() in q or c["month_slug"] in q:
            score += 1
        if c["brand"].lower() in q:
            score += 1
        for s in c["stores"]:
            if s.lower() in q or STORES[s]["location"].lower().split("/")[0].strip() in q:
                score += 2
        if "twinleaf" in q and "Twinleaf" in c["brand"]:
            score += 2
        if ("smokers" in q or "warehouse" in q) and "Smokers" in c["brand"]:
            score += 2
        for token in ["vape", "firework", "sandwich", "coffee", "bagel", "grab", "zyn", "cooler", "pizza", "water", "thunder", "spark"]:
            if token in q and token in (c["title"] + c["id"] + c.get("family", "")).lower():
                score += 2
        if score:
            scored.append((score, c))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [c for _, c in scored]


def summarize_family(f):
    arc = " → ".join(f"{a['month']}: {a['headline']}" for a in f["arc"])
    return (
        f"{f['name']} ({f['brand']} · {', '.join(store_labels(f['stores']))}) runs {', '.join(f['months'])}. "
        f"Offer: {f['offer']}. {f['summary']} Arc: {arc}. Takeaway: {f['takeaway']} Next: {f['recommendation']}"
    )


def summarize_month(m):
    mets = "; ".join(f"{x['label']} {x['value']} ({x['delta']})" for x in m["metrics"])
    return (
        f"{m['month']} — {m['theme']} ({', '.join(m['brands'])}; stores {', '.join(store_labels(m['stores']))}). "
        f"{m['summary']} Highlights: {' '.join(m['highlights'][:3])} "
        f"Metrics: {mets}. Recommendations: {' '.join(m['recommendations'][:2])}"
    )


def summarize_store(store_key: str):
    store = STORES.get(store_key)
    if not store:
        return None
    camps = [c for c in CAMPAIGNS if store_key in c["stores"]]
    bits = []
    for c in camps[:8]:
        bits.append(f"{c['month']} {c['title']}: {metrics_brief(c, 2)}")
    return (
        f"{store['short']} ({store['brand']}) appears in {len(camps)} tracked campaigns May–August. "
        + " | ".join(bits)
    )


def answer_from_knowledge(query: str):
    q = (query or "").lower().strip()
    families = match_families(q)
    months = match_months(q)
    campaigns = match_campaigns(q)

    wants_summary = any(t in q for t in ["summar", "overview", "story", "results", "at a glance", "how did", "overall"])
    wants_recs = any(t in q for t in ["recommend", "next step", "action", "should we", "priority", "q4"])
    wants_family = any(t in q for t in ["family", "across month", "multi-month", "stretch", "continuous", "ongoing"]) or bool(families)
    wants_store = any(k.lower() in q for k in STORES) or any(t in q for t in ["akwesasne", "covington", "express", "store"])

    if wants_family and families:
        f = families[0]
        linked = [campaign_by_id(cid) for cid in f["campaign_ids"] if campaign_by_id(cid)]
        recs = [r for r in RECOMMENDATIONS if f["brand"].split()[0] in r["brand"] or any(s in r["stores"] for s in f["stores"])]
        return summarize_family(f), linked, recs[:3] or RECOMMENDATIONS[:3]

    if months and (wants_summary or "month" in q or months[0]["slug"] in q):
        m = months[0]
        linked = [campaign_by_id(cid) for cid in m["campaign_ids"] if campaign_by_id(cid)]
        return summarize_month(m), linked, [{"title": r, "impact": "Medium", "detail": r, "brand": m["brands"][0], "stores": m["stores"], "timing": m["month"]} for r in m["recommendations"][:3]]

    store_key = next((k for k in STORES if k.lower() in q or STORES[k]["location"].lower().split("/")[0].strip() in q), None)
    if wants_store and store_key:
        text = summarize_store(store_key)
        linked = [c for c in CAMPAIGNS if store_key in c["stores"]][:4]
        return text, linked, RECOMMENDATIONS[:3]

    if campaigns:
        c = campaigns[0]
        store_bits = "; ".join(f"{b['store']}: {b['detail']} ({b['delta']})" for b in c["store_breakdown"])
        answer = (
            f"{c['title']} — {c['month']} · {c['brand']} · {', '.join(store_labels(c['stores']))}. "
            f"Offer: {c['offer']}. {c['summary']} Metrics: {metrics_brief(c, 4)}. By store: {store_bits}. "
            f"Takeaway: {c['takeaway']} Next: {c['recommendation']}"
        )
        return answer, campaigns[:3], RECOMMENDATIONS[:3]

    if wants_recs:
        rec_text = "Top recommendations: " + " ".join(
            f"{i+1}) {r['title']} ({r['brand']} — {', '.join(r['stores'])}): {r['detail']}"
            for i, r in enumerate(RECOMMENDATIONS[:4])
        )
        return rec_text, AUGUST_CAMPAIGNS, RECOMMENDATIONS[:4]

    if wants_summary:
        return executive_summary_answer(), AUGUST_CAMPAIGNS, RECOMMENDATIONS[:3]

    return executive_summary_answer(), AUGUST_CAMPAIGNS, RECOMMENDATIONS[:3]
