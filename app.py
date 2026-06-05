import streamlit as st

# MUST be the first Streamlit command in the script
st.set_page_config(
    page_title="UAE Real Estate AI Prototypes Hub",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded"
)

from src.utils.style import inject_premium_style
from src.tenant_retention.ui import render_tenant_retention_page
from src.content_engine.ui import render_content_engine_page
from src.deal_intelligence.ui import render_deal_intelligence_page

# Inject custom premium styles
inject_premium_style()

# Sidebar branding & navigation
st.sidebar.markdown(
    """
    <div style="text-align: center; margin-bottom: 20px;">
        <h1 style="font-family: 'Playfair Display', serif; color: #D4AF37; margin: 0; font-size: 2.2rem; font-weight:700;">AL-HILAL</h1>
        <div style="font-size: 0.75rem; letter-spacing: 2px; color: #8A99AD; text-transform: uppercase;">Real Estate AI Labs</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.write("---")

# Navigation Selector
page_options = [
    "👑 Portfolio Overview Hub",
    "📊 Tenant Retention Service",
    "✍️ Real Estate Content Engine",
    "💬 Deal Intelligence Simulator"
]

selected_page = st.sidebar.radio(
    "Select AI Application Prototype:",
    page_options,
    index=0
)

st.sidebar.write("---")

# Sidebar educational facts to increase realism
st.sidebar.markdown(
    """
    <div style="background-color: #161A22; border: 1px solid rgba(212,175,55,0.15); border-radius: 8px; padding: 15px; font-size: 0.8rem; line-height: 1.4;">
        <strong style="color: #D4AF37; display: block; margin-bottom: 5px;">🇦🇪 UAE Property Compliance</strong>
        <strong>RERA Tenancy Law:</strong> Lease changes or non-renewals must be served with a statutory 90-day written notice.<br><br>
        <strong>Ejari:</strong> The standardized rental contract registration system in Dubai.<br><br>
        <strong>10-Year Golden Visa:</strong> Investment in properties worth AED 2,000,000 or more is eligible.
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown(
    """
    <div style="text-align: center; font-size: 0.7rem; color: #8A99AD; margin-top: 30px;">
        Al-Hilal AI Labs v1.0.0 (Local Sandbox)<br>
        Powered by Mock-LLM Heuristic Engines
    </div>
    """,
    unsafe_allow_html=True
)

# Route to selected page UI
if selected_page == "👑 Portfolio Overview Hub":
    # Welcome Dashboard landing
    st.markdown('<h1 class="gold-text" style="font-size:3rem; margin-bottom: 0;">Al-Hilal Real Estate AI Suite</h1>', unsafe_allow_html=True)
    st.markdown("##### Premium local AI applications & automated workflows designed for the UAE property sector.")
    st.write("---")
    
    st.markdown(
        """
        <div style="background-image: linear-gradient(135deg, rgba(212, 175, 55, 0.05) 0%, rgba(14, 17, 23, 0.9) 100%); border: 1px solid rgba(212, 175, 55, 0.2); padding: 30px; border-radius: 12px; margin-bottom: 30px; box-shadow: 0 4px 30px rgba(0,0,0,0.4);">
            <h3 style="margin-top:0; color:#D4AF37; font-family:'Playfair Display';">Welcome to the AI Sandbox</h3>
            <p style="font-size: 1.05rem; line-height: 1.6; color: #E2E8F0; max-width: 900px;">
                This workspace contains high-fidelity prototype dashboard systems designed to solve real estate operational challenges in Dubai. 
                Using localized regulatory compliance (RERA index matrices, Ejari timelines) and dynamic templating, these apps run completely 
                offline on local mock data and rule engines without requiring paid API tokens.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.subheader("Explore Available Prototypes")
    
    # 3-column layout showcasing the apps
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(
            """
            <div class="luxury-card" style="height: 380px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <h3 style="color:#D4AF37; margin-top:0;">1. Tenant Retention</h3>
                    <p style="font-size:0.9rem; color:#8A99AD; line-height:1.5;">
                        A predictive analytics dashboard tracking Dubai lease expirations and compliance milestones. 
                        Calculates an automated vacancy risk percentage and offers a one-click renewal letter generator using legal RERA index rules.
                    </p>
                    <ul style="font-size:0.85rem; padding-left:20px; color:#E2E8F0;">
                        <li>Ejari milestone countdowns</li>
                        <li>RERA rent cap evaluations</li>
                        <li>Automated lease offer builder</li>
                    </ul>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Launch Tenant Retention Service", key="btn_retention", use_container_width=True):
            # We set sidebar navigation states
            st.info("👈 Use the sidebar navigation menu to switch to the **Tenant Retention Service** page.")
            
    with col2:
        st.markdown(
            """
            <div class="luxury-card" style="height: 380px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <h3 style="color:#D4AF37; margin-top:0;">2. Content Engine</h3>
                    <p style="font-size:0.9rem; color:#8A99AD; line-height:1.5;">
                        A media generator dashboard. Simulates parsing developer PDF/text files (such as project floor plans and brochures) 
                        to synthesize localized multichannel marketing copy.
                    </p>
                    <ul style="font-size:0.85rem; padding-left:20px; color:#E2E8F0;">
                        <li>IG Reel cinematic storyboard script</li>
                        <li>Investor B2B LinkedIn posts</li>
                        <li>Bilingual WhatsApp copy</li>
                        <li>Formal email campaign layout</li>
                    </ul>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Launch Content Engine", key="btn_content", use_container_width=True):
            st.info("👈 Use the sidebar navigation menu to switch to the **Real Estate Content Engine** page.")
            
    with col3:
        st.markdown(
            """
            <div class="luxury-card" style="height: 380px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <h3 style="color:#D4AF37; margin-top:0;">3. Deal Intelligence</h3>
                    <p style="font-size:0.9rem; color:#8A99AD; line-height:1.5;">
                        A live split-screen simulator mimicking a customer chatting on WhatsApp. The AI parser extracts budgets, nationalities, 
                        and intent parameters in real-time, displaying them in a live Lead Dossier alongside automated developer inventory matching.
                    </p>
                    <ul style="font-size:0.85rem; padding-left:20px; color:#E2E8F0;">
                        <li>WhatsApp mockup layout</li>
                        <li>Heuristic entity extractor</li>
                        <li>Lead scoring (1-100)</li>
                        <li>Inventory match list</li>
                    </ul>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Launch Deal Intelligence", key="btn_deal", use_container_width=True):
            st.info("👈 Use the sidebar navigation menu to switch to the **Deal Intelligence Simulator** page.")

elif selected_page == "📊 Tenant Retention Service":
    render_tenant_retention_page()
    
elif selected_page == "✍️ Real Estate Content Engine":
    render_content_engine_page()
    
elif selected_page == "💬 Deal Intelligence Simulator":
    render_deal_intelligence_page()
