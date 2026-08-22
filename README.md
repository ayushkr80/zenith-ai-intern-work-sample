# StylePilot — AI Fashion Recommendation POC

An independent fashion recommendation proof-of-concept developed as a work sample for the **Zenith / J.E.R.K. AI Internship assignment**.

StylePilot explores how **colour profile, style direction, occasion, climate, and budget** can be combined to generate a more relevant and explainable fashion recommendation.

> **Note:** This is an independent proof-of-concept. It does not reproduce, access, or claim to use proprietary Zenith/J.E.R.K. models, datasets, APIs, algorithms, or internal systems.

---

## 🎯 Project Overview

The idea behind StylePilot is to move beyond generic fashion suggestions by considering multiple aspects of a user's context.

The current prototype takes five inputs:

- Colour profile
- Style direction
- Occasion
- Climate
- Approximate outfit budget

These inputs are processed through a transparent recommendation layer to generate:

- A recommended outfit direction
- A suggested colour palette
- A short explanation of the recommendation
- Structured user feedback

The prototype is intentionally designed as a simple, explainable baseline that can be extended into a more advanced personalization system.

---

## 🧠 Recommendation Approach

```text
Colour Profile
      +
Style Direction
      +
Occasion
      +
Climate
      +
Budget
      ↓
Recommendation Logic
      ↓
Recommended Outfit
      +
Colour Palette
      +
Explanation
      ↓
User Feedback
