# Al-Hilal UAE Real Estate AI Suite (Prototypes Monorepo)

A local Python-based monorepo containing interactive prototypes for three UAE real estate AI systems. Built with **Streamlit** using custom CSS overrides for a premium, dark-gold luxury branding theme. All applications utilize specialized rule engines and localized templates, requiring no external paid API keys.

---

## 🏗️ Folder Structure

```
d:/uae-realestate-prototypes/
├── requirements.txt            # Python dependencies (streamlit, pandas, numpy, plotly)
├── app.py                      # Main Streamlit launcher (routing & navigation hub)
├── .gitignore                  # Git ignore file
├── README.md                   # Documentation
└── src/
    ├── __init__.py
    ├── utils/
    │   ├── __init__.py
    │   └── style.py            # Luxury UAE Real Estate CSS style injector
    ├── tenant_retention/
    │   ├── __init__.py
    │   ├── data.py             # Mock Dubai tenancy databases
    │   ├── logic.py            # Vacancy risk scoring & Dubai RERA renewal offer letters
    │   └── ui.py               # Milestone timeline dashboard & offer generator workspace
    ├── content_engine/
    │   ├── __init__.py
    │   ├── logic.py            # Simulated PDF parser & social collateral generators
    │   └── ui.py               # File uploader simulator & copywriting workspace
    └── deal_intelligence/
        ├── __init__.py
        ├── logic.py            # WhatsApp text entity parser & lead scorer (1-100)
        └── ui.py               # WhatsApp mockup simulator & live Agent Dashboard
```

---

## 🌟 Featured Applications

### 📊 1. Tenant Retention Service
*   **Predictive Dashboard:** Tracks annual rents, lease countdowns, and maintenance issues.
*   **Vacancy Risk Scoring:** Calculates risk based on complaints, lease urgency, and RERA price margins.
*   **Contract Milestones:** Visualizes legal UAE milestone deadlines (90-day warning, negotiation, and sign-offs).
*   **Renewal Proposal Generator:** Dynamically creates lease offer letters conforming to Dubai Tenancy Law No. 26 of 2007 (and amendment Law No. 33 of 2008).

### ✍️ 2. Real Estate Content Engine
*   **Brochure Uplink:** Simulates scanning developer text and brochures.
*   **Editable Metadata Form:** Enables customization of prices, payment structures, handovers, and amenities.
*   **Multichannel Script Sync:**
    *   **Instagram Reel:** Full script with audio instructions, cinematic shot cue boards, and hashtags.
    *   **LinkedIn Update:** Professional, B2B investment outline highlighting cash-on-cash ROI.
    *   **WhatsApp Templates:** Eng/Arb high-conversion messages side-by-side.
    *   **Investor Newsletter:** Formal email template ready to send.

### 💬 3. Deal Intelligence Simulator
*   **WhatsApp Chat UI:** A mockup window where users can type messages or run pre-loaded scenarios.
*   **Live Parameter Extractor:** Scans conversations for budgets (normalizing to AED), nationalities, and purchase purposes (Investment vs. End-user).
*   **Lead Dossier:** Automatically grades lead quality on a 1-100 score.
*   **Listing Matcher:** Recommends appropriate Dubai developments matching buyer budgets.

---

## 🚀 Local Setup Instructions

1.  **Clone / Open the workspace directory:**
    ```bash
    cd d:/uae-realestate-prototypes
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application launcher:**
    ```bash
    streamlit run app.py
    ```

4.  **Open your browser:**
    Navigate to [http://localhost:8501](http://localhost:8501) to explore the interactive suite.
