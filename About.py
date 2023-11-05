import streamlit as st
from streamlit_login_auth_ui.widgets import __login__
from dotenv import load_dotenv
import os
from streamlit_lottie import st_lottie

load_dotenv()

__login__obj = __login__(
    auth_token=os.getenv("CORIAR"),
    company_name="Tianji",
    width=200,
    height=250,
    logout_button_name="Logout",
    hide_menu_bool=False,
    hide_footer_bool=False,
    lottie_url="https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json",
)

LOGGED_IN = __login__obj.build_login_ui()

if LOGGED_IN == True:
    st.write(
        "<h1 style='color: white; font-size: 24px; font-weight: bold;'>Meet your Personal AI Nutritionist & Chef-bot 👋</h1>",
        unsafe_allow_html=True,
    )

    st.write(
        "<h1 style='text-align: center; color: red; font-size: 92px; font-family: cursive, 'Dancing Script', cursive; font-weight: bold;'>Nutri AI</h1>",
        unsafe_allow_html=True,
    )

    st_lottie(
        "https://lottie.host/4bed853f-afa3-4536-905d-0af860bbdefc/Zajmp9Z8LS.json"
    )
