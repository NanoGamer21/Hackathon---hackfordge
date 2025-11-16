import streamlit as st
import requests, urllib.parse, secrets

# Page configuration
st.set_page_config(page_title="Aztec Reserve", page_icon="🎓")

# Google OAuth credentials from secrets
CLIENT_ID = st.secrets["google"]["client_id"]
CLIENT_SECRET = st.secrets["google"]["client_secret"]
REDIRECT_URI = st.secrets["google"]["redirect_uri"]

# OAuth endpoints
AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_URL = "https://oauth2.googleapis.com/token"
USERINFO_URL = "https://www.googleapis.com/oauth2/v3/userinfo"

def login_link(state):
    params = {
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": "openid email profile",
        "access_type": "offline",
        "prompt": "consent",
        "state": state,
        "hd": "sdsu.edu",
    }
    return f"{AUTH_URL}?{urllib.parse.urlencode(params)}"

def exchange_code(code):
    data = {
        "code": code,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code",
    }
    r = requests.post(TOKEN_URL, data=data, timeout=15)
    r.raise_for_status()
    return r.json()

def get_user_info(token):
    r = requests.get(USERINFO_URL, headers={"Authorization": f"Bearer {token}"}, timeout=15)
    r.raise_for_status()
    return r.json()

# Create state token if not present
if "state" not in st.session_state:
    st.session_state.state = secrets.token_urlsafe(16)

# Handle OAuth callback using the new query params API
_raw_code = st.query_params.get("code")
code = _raw_code[0] if isinstance(_raw_code, list) else _raw_code
if code:
    try:
        tokens = exchange_code(code)
        user = get_user_info(tokens["access_token"])
        email = (user.get("email") or "").lower()
        if email.endswith("@sdsu.edu"):
            st.session_state.user = user
            st.query_params.clear()  # clear the query params
            # Redirect to SearchP page after login (must live at pages/SearchP.py)
            st.switch_page("pages/SearchP.py")
        else:
            st.error("Only @sdsu.edu accounts allowed. Please switch accounts.")
    except Exception as e:
        st.error(f"Login failed: {e}")

# UI: same fonts and (default) background behavior as Search page
st.markdown(
    """
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Merriweather:wght@700;900&display=swap');

      /* Match Search page typography */
      html, body, [data-testid="stAppViewContainer"]{
        font-family: "Inter", system-ui, -apple-system, Segoe UI, Roboto, sans-serif !important;
        -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale;
      }
      h1, h2, h3, h4, h5, h6{
        font-family: "Merriweather", Georgia, "Times New Roman", serif !important;
        letter-spacing: .2px;
      }

      /* No background overrides: use Streamlit theme (same as Search page) */

      /* Header block */
      .header-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 40px;
      }
      .header-inner {
        display: flex;
        align-items: center;
        gap: 15px;
      }
      .header-inner h1 {
        margin: 0;
        font-size: 38px;
      }

      /* Transparent Google sign-in button (no inner border) */
      .sdsu-login {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        padding: 12px 20px;
        border-radius: 8px;
        border: 0;                 /* no inner border so we only see the card border */
        font-size: 16px;
        font-weight: 600;
        text-decoration: none;
        background: transparent;
        color: inherit;            /* follow page text color */
        box-shadow: none;
        transition: background-color .2s ease, transform .05s ease;
        cursor: pointer;
      }
      .sdsu-login:hover { background: rgba(0,0,0,0.05); }
      .sdsu-login:active { transform: translateY(1px); }

      /* Keep the Google icon readable */
      .sdsu-login img {
        background: #fff;
        border-radius: 50%;
        padding: 2px;
      }

      /* Center wrapper */
      .center {
        display: flex;
        justify-content: center;
        margin-top: 60px;
      }

      /* SINGLE subtle outer border around the whole area */
      .login-card {
        border: 1px solid #e5e5e5;   /* subtle light border to match default theme */
        border-radius: 12px;
        padding: 20px 24px;
      }
    </style>

    <div class="header-container">
      <div class="header-inner">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/San_Diego_State_University_primary_logo.svg/2560px-San_Diego_State_University_primary_logo.svg.png"
             width="240" style="margin-top:-6px;">
        <h1>Aztec Reserve</h1>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# If user is already logged in
if "user" in st.session_state:
    u = st.session_state.user
    st.success(f"Welcome, {u.get('name') or u.get('email')} ✅")
    st.caption(u.get("email", ""))
    if st.button("Go to Search", use_container_width=True):
        st.switch_page("pages/SearchP.py")
    st.divider()
    st.header("Protected area")
    st.write("Only SDSU-authenticated users can see this content.")
else:
    url = login_link(st.session_state.state)
    st.markdown(
        f"""
        <div class="center">
          <div class="login-card">
            <a href="{url}" class="sdsu-login" role="button" aria-label="Sign in with SDSU">
              <img src="https://www.gstatic.com/firebasejs/ui/2.0.0/images/auth/google.svg"
                   width="22" height="22" alt="Google logo">
              Sign in with SDSU
            </a>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

