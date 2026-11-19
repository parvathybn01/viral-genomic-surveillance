        <a class="phw-resource" href="https://www.who.int/emergencies/disease-outbreak-news" target="_blank" rel="noopener noreferrer">
          <span class="phw-resource-tag">Official updates</span><strong>WHO Disease Outbreak News</strong><span class="phw-desc">Read official communications about selected public-health events.</span><span class="phw-link">View outbreak news ↗</span>
        </a>
        <a class="phw-resource" href="https://www.ncbi.nlm.nih.gov/labs/virus/" target="_blank" rel="noopener noreferrer">
          <span class="phw-resource-tag">Sequence database</span><strong>NCBI Virus</strong><span class="phw-desc">Explore viral sequence records and related scientific information.</span><span class="phw-link">Explore sequence resources ↗</span>
        </a>
      </div>
      <div class="phw-note"><div class="phw-note-mark">i</div><div><strong>Important limitation</strong>
        <p>VIGESORA is a research-support prototype. Its configured classifier covers only its supported classes; it does not diagnose infection, recommend an individual treatment, or forecast outbreaks from a single genome.</p></div></div>
    </div>
    """, unsafe_allow_html=True)
    render_updates()
    if st.button("Return to VIGESORA home", type="secondary", key="phw_return_home"):
        navigate("Home")
    render_footer()


GUIDES = {
    "Getting Started": [
        ("What VIGESORA does", "VIGESORA brings together variant-classification workflows, scientific evidence, and accessible public-health resources."),
        ("Choose a portal", "Use Genomic Sandbox for researcher-oriented workflows and Public Health Watch for accessible information and official resources."),
        ("Prototype limitations", "Demo outputs are illustrative. Actual variant predictions require the backend API; a prediction among Alpha, Beta, Gamma, and Omicron does not cover all possible lineages."),
    ],
    "Researcher / Lab Guide": [
        ("Prepare a FASTA file", "A FASTA file should contain one header line beginning with > followed by sequence lines. Use data you are authorized to analyse."),
        ("Upload and validate", "Open New Analysis and select a FASTA file. Basic structure and ambiguity information is shown automatically. These checks do not prove biological validity."),
        ("Read the results", "Review the predicted class, available class scores, sequence length, sequence-quality indicators, variant information, and backend warnings."),
        ("Save and export", "Download the JSON report or save a session-level record. Persistent storage is not connected in this prototype."),
    ],
    "Public Health Guide": [
        ("Use trusted sources", "Prefer official public-health agencies and peer-reviewed evidence for current surveillance information."),
        ("Check context and date", "Review the source, publication date, population, method, and uncertainty before drawing conclusions."),
    ],
    "Scientific Terminology & FAQ": [
        ("Genome sequence", "The ordered genetic letters representing a virus's genetic material."),
        ("Ambiguous bases", "Sequence positions that do not identify one unambiguous A, C, G, or T base. Their meaning depends on the symbol and workflow."),
        ("Model confidence", "A model output score. It is not automatically a calibrated probability that a prediction is correct."),
        ("Variant classification", "A model's prediction among the classes it was trained to represent. It is not necessarily a formal lineage assignment."),
        ("Risk indicator", "A measure based on specified evidence or a model. It should not be interpreted as a prediction without suitable validation."),
    ],
    "Privacy": [
        ("Uploaded sequences", "In Demo mode, files are processed only inside this Streamlit session. In Live Flask API mode, the file is sent to the backend URL you enter, so only use a backend you trust."),
        ("Stored data", "Saved analyses and activity are kept in session memory only and are lost when the session ends. No database is connected."),
        ("Sign-in", "Sign-in is a placeholder. Do not enter a real password."),
    ],
}


def render_help():
    render_header()
    st.markdown('<div class="section"><div class="eyebrow">Support</div><h1 class="heading">Help & Guidelines</h1>'
                '<p class="intro">Choose a guide to learn how to use VIGESORA and interpret its information responsibly.</p></div>', unsafe_allow_html=True)
    descriptions = {
        "Getting Started": "Learn the purpose of VIGESORA and how to navigate its portals.",
        "Researcher / Lab Guide": "Prepare FASTA files and understand the analysis workflow.",
        "Public Health Guide": "Explore surveillance resources and interpret public-facing information.",
        "Scientific Terminology & FAQ": "Understand common genomic and surveillance terms and their limitations.",
        "Privacy": "How uploaded data and saved records are handled in this prototype.",
    }
    for title, desc in descriptions.items():
        st.markdown(f'<div><strong>{title}</strong><div class="small-note">{desc}</div></div>', unsafe_allow_html=True)
        if st.button(f"Open {title}", key=f"open_guide_{title}", type="secondary"):
            st.session_state.guide = title
            navigate("Guide")
    render_footer()


def render_guide():
    render_header()
    title = st.session_state.guide
    st.markdown(f'<div class="section"><div class="eyebrow">Help & Guidelines</div><h1 class="heading">{escape(title)}</h1>'
                '<p class="intro">A practical guide to using VIGESORA responsibly.</p></div>', unsafe_allow_html=True)
    for heading, body in GUIDES.get(title, GUIDES["Getting Started"]):
        st.markdown(f"### {heading}")
        st.write(body)
    if st.button("← Back to Help & Guidelines", type="secondary"):
        navigate("Help")
    render_footer()


# ---------------------------------------------------------------------------
# Sidebar navigation (keyed radio + callback so it never overwrites login pages)
# ---------------------------------------------------------------------------
NAV_OPTIONS = ["Home", "Research Overview", "New Analysis", "Analysis Results", "Public Health Watch", "Help & Guidelines"]
PAGE_TO_NAV = {
    "Home": "Home",
    "Choose portal": "Home",
    "Sign in": "Home",
    "Research Overview": "Research Overview",
    "New Analysis": "New Analysis",
    "Analysis Results": "Analysis Results",
    "Public Health Watch": "Public Health Watch",
    "Help": "Help & Guidelines",
    "Guide": "Help & Guidelines",
}


def on_nav_change():
    label = st.session_state.nav_radio
    st.session_state.page = "Help" if label == "Help & Guidelines" else label


with st.sidebar:
    st.markdown(
        f'<div class="sidebar-logo-wrap"><img class="sidebar-vigesora-logo" src="{VIGESORA_LOGO_DATA_URI}" alt="VIGESORA logo" /></div>',
        unsafe_allow_html=True,
    )
    st.caption("Viral genomic surveillance")
    st.session_state.nav_radio = PAGE_TO_NAV.get(st.session_state.page, "Home")
    st.radio("Navigate", NAV_OPTIONS, key="nav_radio", on_change=on_nav_change, label_visibility="collapsed")
    st.divider()
    st.markdown("**Workspace status**")
    st.caption("Frontend prototype")
    st.caption("Backend: " + ("Configured" if os.getenv("VIGESORA_API_URL") else "Set API URL in New Analysis"))


# ---------------------------------------------------------------------------
# Router
# ---------------------------------------------------------------------------
routes = {
    "Home": render_home,
    "Choose portal": render_choose_portal,
    "Sign in": render_signin,
    "Research Overview": render_research_overview,
    "New Analysis": render_new_analysis,
    "Analysis Results": render_results,
    "Public Health Watch": render_public_watch,
    "Help": render_help,
