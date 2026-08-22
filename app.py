import streamlit as st

st.set_page_config(page_title="StylePilot", page_icon="👕")
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

def recommend(profile, occasion, climate, style, budget):
    palette = PALETTES[profile]
    fabric = {"Hot":"cotton / linen", "Mild":"cotton / light twill", "Cold":"wool blend / layered cotton"}[climate]
    if occasion == "Formal":
        outfit = f"{palette[0]} {fabric} shirt + tailored trousers + minimal footwear"
    else:
        outfit = f"{STYLES[style]} using {fabric}"
    budget_band = "Value" if budget < 2000 else "Mid-range" if budget < 5000 else "Premium"
    reasons = [
        f"{profile} palette: {', '.join(palette[:3])}",
        f"Climate: {climate} → {fabric}",
        f"Occasion: {occasion}",
        f"Style: {style}",
        f"Budget: {budget_band}"
    ]
    return outfit, palette, reasons

st.title("StylePilot")
st.caption("Independent AI-fashion product proof of concept")
st.info("This is an independent POC inspired by the public-facing assignment. It does not reproduce or claim to use proprietary Zenith/J.E.R.K. models or data.")

profile = st.selectbox("Colour profile", ["Warm", "Cool", "Neutral"])
occasion = st.selectbox("Occasion", ["Casual", "Smart Casual", "Formal"])
climate = st.selectbox("Climate", ["Hot", "Mild", "Cold"])
style = st.selectbox("Style direction", list(STYLES))
budget = st.slider("Approx. outfit budget (₹)", 1000, 10000, 3000, 500)

if st.button("Generate recommendation", type="primary"):
    outfit, palette, reasons = recommend(profile, occasion, climate, style, budget)
    st.subheader("Recommended direction")
    st.write(outfit)
    st.subheader("Palette")
    st.write(" • ".join(palette))
    st.subheader("Why?")
    for r in reasons:
        st.write("✓ " + r)

    st.divider()
    feedback = st.radio("Quick feedback", ["Looks good", "Change colours", "Change fit", "Too expensive"], horizontal=True)
    if st.button("Save feedback"):
        st.success(f"Structured feedback captured: {feedback}")
