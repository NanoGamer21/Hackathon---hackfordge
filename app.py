import streamlit as st
import requests, urllib.parse, secrets

# Page configuration
st.set_page_config(page_title="Room Reserve", page_icon="🎓")

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

# Handle OAuth callback
qs = st.experimental_get_query_params()
if "code" in qs:
    try:
        tokens = exchange_code(qs["code"][0])
        user = get_user_info(tokens["access_token"])
        email = (user.get("email") or "").lower()
        if email.endswith("@sdsu.edu"):
            st.session_state.user = user
            st.experimental_set_query_params()  # clear the query params
            # Redirect to SearchP page after login
            try:
                st.switch_page("pages/SearchP.py")
            except Exception:
                # fallback: just show a link if switch_page isn't supported
                st.markdown("[Continue to Search Page →](pages/SearchP.py)", unsafe_allow_html=True)
        else:
            st.error("Only @sdsu.edu accounts allowed. Please switch accounts.")
    except Exception as e:
        st.error(f"Login failed: {e}")

# UI: Header with logo + title
st.markdown(
    """
    <style>
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
            font-family: sans-serif;
            font-size: 38px;
        }
    </style>
    <div class="header-container">
        <div class="header-inner">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/San_Diego_State_University_primary_logo.svg/2560px-San_Diego_State_University_primary_logo.svg.png"
                 width="280" style="margin-top:-10px;">
            <h1>Room Reserve</h1>
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
    # Show a link button to search page also
    st.page_link("pages/SearchP.py", label="Go to Search", icon="🔎")
    if st.button("Sign out"):
        st.session_state.pop("user", None)
        st.experimental_set_query_params()
    st.divider()
    st.header("Protected area")
    st.write("Only SDSU-authenticated users can see this content.")
else:
    url = login_link(st.session_state.state)
    st.markdown(
        f"""
        <style>
        .sdsu-login {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            padding: 12px 20px;
            background-color: #C41E3A;
            color: white;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 600;
            text-decoration: none;
            transition: background-color 0.2s ease;
        }}
        .sdsu-login:hover {{ background-color: #a9152f; }}
        .sdsu-login img {{
            background: white;
            border-radius: 50%;
            padding: 2px;
        }}
        .center {{
            display: flex;
            justify-content: center;
            margin-top: 60px;
        }}
        </style>
        <div class="center">
            <a href="{url}" class="sdsu-login">
                <img src="https://www.gstatic.com/firebasejs/ui/2.0.0/images/auth/google.svg"
                     width="22" height="22">
                Sign in with SDSU
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

