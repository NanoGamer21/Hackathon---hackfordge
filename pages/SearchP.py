import streamlit as st

# Page configuration
st.set_page_config(page_title="Search a Subject", page_icon="🔎", layout="centered")

# --- CSS: SDSU red full-page background + theme-aware button contrast ---
st.markdown(
    """
    <style>
        :root {
            --sdsu-red: #C41E3A;
            --sdsu-red-dark: #a9152f;
        }

        /* Force the whole app background to SDSU red to match the login screen */
        html, body, .stApp, .main, .block-container {
            background-color: var(--sdsu-red) !important;
            color: #ffffff !important;
            min-height: 100vh;
        }

        /* Make the centered container a little translucent so controls are visible */
        .stApp .main .block-container {
            padding-top: 24px;
        }

        /* Header area adjustments - top-left header */
        .top-left-header {
            display: flex;
            align-items: center;
            gap: 12px;
            margin: 0;
        }
        .top-left-header img {
            display: block;
            margin: 0;
        }
        .top-left-title {
            margin: 0;
            line-height: 1;
        }
        .top-left-subtitle {
            font-size: 0.95rem;
            opacity: 0.9;
            margin-top: 2px;
        }

        /* Keep inputs readable by using white backgrounds for inputs */
        .stTextInput>div>div>input,
        .stSelectbox>div>div>select,
        .stButton>button,
        .stNumberInput>div>input,
        .stDateInput>div>div>input,
        .stTimeInput>div>div>input {
            background: rgba(255,255,255,0.95) !important;
            color: #000000 !important;
            border-radius: 6px;
        }

        /* Sign out button style (keeps contrast in both modes) */
        .stButton>button[title="sign_out_button"] {
            border-radius: 8px;
        }

        /* Make sure links remain visible */
        a { color: #ffffff; }

        /* Light-mode: keep SDSU red as page bg and white text, buttons red */
        @media (prefers-color-scheme: light), (prefers-color-scheme: no-preference) {
            .stButton>button { background-color: rgba(0,0,0,0.06) !important; color: #000 !important; }
        }

        /* Dark-mode: adjust button text color for readability */
        @media (prefers-color-scheme: dark) {
            .stButton>button { background-color: #ffffff !important; color: var(--sdsu-red) !important; }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Require login
if "user" not in st.session_state:
    st.error("Please sign in with your @sdsu.edu account to continue.")
    st.stop()

# Top row: header on the left (SDSU Room Reserve) and sign out on the right
cols = st.columns([6, 1])
with cols[0]:
    # Top-left header: SDSU logo + "Room Reserve" title and small subheading
    st.markdown(
        """
        <div class="top-left-header">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/San_Diego_State_University_primary_logo.svg/2560px-San_Diego_State_University_primary_logo.svg.png"
                 width="140" style="margin-top:0;">
            <div>
                <h1 class="top-left-title" style="margin:0; font-family:sans-serif; color:#ffffff;">Room Reserve</h1>
                <div class="top-left-subtitle" style="color:#ffffff;">Search a Subject</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with cols[1]:
    # Sign out functionality (clears session and reruns)
    if st.button("Sign out", key="sign_out_button"):
        keys_to_keep = {"state"} if "state" in st.session_state else set()
        for k in list(st.session_state.keys()):
            if k not in keys_to_keep:
                del st.session_state[k]
        st.experimental_rerun()

st.write("")  # spacing

# Topics list (preserve your design / content)
topics = [
    "Dungeons & Dragons",
    "CS Study Sesh",
    "LOCKIN IN ON EXAMS",
    "Math Club",
    "Clash Royale"
]
topics = sorted(topics, key=str.casefold)

# Dropdown
choice = st.selectbox(
    "Choose a topic (type to filter):",
    options=topics,
    index=None,
    placeholder="Search"
)

# Create button (keep behavior)
if st.button("Create an Event!", use_container_width=True):
    st.write(f"Event created for: {choice}")