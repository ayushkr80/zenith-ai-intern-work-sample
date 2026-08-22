import streamlit as st

# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="StylePilot",
    page_icon="👕",
    layout="centered"
)

# ---------------------------------------------------------
# Data
# ---------------------------------------------------------
PALETTES = {
    "Warm": ["Olive", "Terracotta", "Cream", "Chocolate", "Mustard"],
    "Cool": ["Navy", "Burgundy", "Charcoal", "Emerald", "Dusty Blue"],
    "Neutral": ["Cream", "Black", "Taupe", "Denim", "Forest Green"],
}

STYLES = {
    "Minimal": "Clean overshirt + plain tee + straight trousers",
    "Streetwear": "Relaxed hoodie + wide trousers + sneakers",
    "Smart Casual": "Textured shirt + tailored trousers + clean sneakers",
    "Traditional": "Solid kurta + tapered trousers + minimal footwear",
}

FABRICS = {
    "Hot": "cotton / linen",
    "Mild": "cotton / light twill",
    "Cold": "wool blend / layered cotton",
}

# ---------------------------------------------------------
# Recommendation engine
# ---------------------------------------------------------
def recommend(profile, occasion, climate, style, budget):
    palette = PALETTES[profile]
    fabric = FABRICS[climate]

    if occasion == "Formal":
        outfit = (
            f"{palette[0]} {fabric} shirt + "
            f"tailored trousers + minimal footwear"
        )
    elif occasion == "Smart Casual":
        outfit = (
            f"{STYLES['Smart Casual']} using {fabric}"
        )
    else:
        outfit = f"{STYLES[style]} using {fabric}"

    if budget < 2000:
        budget_band = "Value"
    elif budget < 5000:
        budget_band = "Mid-range"
    else:
        budget_band = "Premium"

    reasons = [
        f"{profile} colour profile → {', '.join(palette[:3])}",
        f"{climate} climate → recommended {fabric}",
        f"{occasion} occasion → context-appropriate outfit",
        f"{style} style direction → personalized styling",
        f"₹{budget:,} budget → {budget_band} positioning",
    ]

    return outfit, palette, reasons


# ---------------------------------------------------------
# Session state
# ---------------------------------------------------------
if "recommendation" not in st.session_state:
    st.session_state.recommendation = None

if "feedback_saved" not in st.session_state:
    st.session_state.feedback_saved = False


# ---------------------------------------------------------
# Header
# ---------------------------------------------------------
st.title("👕 StylePilot")
st.caption("AI-fashion recommendation proof of concept")

st.info(
    "Independent POC created for the Zenith/J.E.R.K. AI internship "
    "assignment. This prototype uses transparent recommendation logic "
    "and does not reproduce or claim access to proprietary models, "
    "datasets, or internal systems."
)

st.divider()


# ---------------------------------------------------------
# User inputs
# ---------------------------------------------------------
st.subheader("Build your look")

col1, col2 = st.columns(2)

with col1:
    profile = st.selectbox(
        "Colour profile",
        ["Warm", "Cool", "Neutral"]
    )

    occasion = st.selectbox(
        "Occasion",
        ["Casual", "Smart Casual", "Formal"]
    )

    climate = st.selectbox(
        "Climate",
        ["Hot", "Mild", "Cold"]
    )

with col2:
    style = st.selectbox(
        "Style direction",
        list(STYLES.keys())
    )

    budget = st.slider(
        "Approx. outfit budget (₹)",
        min_value=1000,
        max_value=10000,
        value=3000,
        step=500
    )

    st.caption(
        f"Selected budget: ₹{budget:,}"
    )


# ---------------------------------------------------------
# Generate recommendation
# ---------------------------------------------------------
if st.button(
    "✨ Generate recommendation",
    type="primary",
    use_container_width=True
):
    outfit, palette, reasons = recommend(
        profile,
        occasion,
        climate,
        style,
        budget
    )

    st.session_state.recommendation = {
        "outfit": outfit,
        "palette": palette,
        "reasons": reasons
    }

    st.session_state.feedback_saved = False


# ---------------------------------------------------------
# Display recommendation
# ---------------------------------------------------------
if st.session_state.recommendation:

    recommendation = st.session_state.recommendation

    st.divider()

    st.subheader("🎯 Recommended direction")

    st.success(recommendation["outfit"])

    # -----------------------------------------------------
    # Palette
    # -----------------------------------------------------
    st.subheader("🎨 Suggested colour palette")

    palette_cols = st.columns(len(recommendation["palette"]))

    for col, colour in zip(
        palette_cols,
        recommendation["palette"]
    ):
        with col:
            st.markdown(
                f"""
                <div style="
                    padding:12px;
                    border-radius:10px;
                    border:1px solid #444;
                    text-align:center;
                    margin-bottom:10px;
                ">
                    <b>{colour}</b>
                </div>
                """,
                unsafe_allow_html=True
            )

    # -----------------------------------------------------
    # Reasoning
    # -----------------------------------------------------
    st.subheader("💡 Why this recommendation?")

    for reason in recommendation["reasons"]:
        st.write(f"✓ {reason}")

    st.divider()

    # -----------------------------------------------------
    # Feedback
    # -----------------------------------------------------
    st.subheader("🔄 Improve the next recommendation")

    feedback = st.radio(
        "What would you change?",
        [
            "Looks good",
            "Change colours",
            "Change fit",
            "Too expensive"
        ],
        horizontal=True
    )

    if st.button(
        "Save feedback",
        use_container_width=True
    ):
        st.session_state.feedback_saved = True

    if st.session_state.feedback_saved:
        st.success(
            f"Feedback captured: **{feedback}**"
        )


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------
st.divider()

st.caption(
    "StylePilot is an independent proof-of-concept demonstrating "
    "context-aware fashion recommendation and a foundation for "
    "future personalization."
)
