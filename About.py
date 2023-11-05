import streamlit as st
from streamlit_login_auth_ui.widgets import __login__
from dotenv import load_dotenv
import os

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
    st.write("# Welcome to Insert name Here! 👋")

    st.markdown(
        """
        Our motivation for creating an AI chatbot that serves as our chief, recipe generator, and meal planner stems from our desire for convenient, personalized, and enjoyable cooking experiences. By providing the chatbot with our dietary requirements, available ingredients, and time constraints, we aim to receive tailored recipe suggestions that suit our needs and preferences, enhancing our daily meals. Additionally, the chatbot's capability to recommend nearby supermarkets and grocery options based on our information not only simplifies the shopping process but also promotes healthy and efficient meal planning. Looking ahead, we envision the chatbot evolving to assist with meal delivery or pickup orders, further streamlining our culinary journey and making cooking a delightful and stress-free endeavor.
        """
    )
