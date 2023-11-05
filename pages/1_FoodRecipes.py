import streamlit as st
from dotenv import load_dotenv
import os
import openai
import pandas as pd
import folium
from streamlit_folium import st_folium
import streamlit_ext as ste
from streamlit_login_auth_ui.widgets import __login__
import re


load_dotenv()

# Set up your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize conversation history as an empty list
conversation_history = []


def miles_to_meter(miles):
    """miles to meter conversion"""
    return miles * 1_609.344


def dalle(input_promt):
    """gets an image with openai"""
    response = openai.Image.create(prompt=input_promt, n=1, size="256x256")
    return response["data"][0]["url"]


def get_completion(messages, model="gpt-3.5-turbo-16k"):
    """grabs completion"""
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.1,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


def main():
    """main entry point"""
    st.title("Nutri AI, Your Personal Nutritionist")

    # Get user input using a text input field
    text = st.text_input("Get your next healthy recipe:")

    # Check if the user has entered a prompt
    if text:
        # Perform actions similar to your Flask app
        # need to give a better prompt
        prompt_answer = f"""
        See if the input provided is relevant and if not assume a healthy dish by yourself and proceed. No need to write anything at this stage.
        If the specific dish is not clear, assume a healthy dish and proceed and write \
        'We want you to eat healthy and here is our recommendation for you.' Use the assumed dish and directly skip to output.

        
        Perform the following actions but make sure not to display them in output:
            1 - If any ingredient is not healthy, tell them that ingredient is not healthy \
                Make sure to memorize healthy ingredients mentioned in the input. If nothing is mentioned or no ingredient is healthy, assume a healthy dish and proceed.
            2 - Look up all memories and summarize the list of ingredients which are healthy along with the healthy ingredients.
            3 - Provide the name of a specific healthy dish that is popular in recipe books and list all the ingredients.
            4 - Answer questions in the formation part, if not asked skip the step
            5 - Make the cost as low as possible for the best meal
            6 - For the `Recipe and Instructions` part, we want the formation to be:   

            
            Only the following output has to be displayed and nothing else before this should be displayed in the output. Please think carefully before sending your reccomendation back. Make sure all the following is displayed.
            Use the following format below and only take this format in the same order as mentioned below, if no instruction is given, assume some healthy dish and proceed.:\
            
    .       Dish Name : <Provide a dish name closely matching the name of the dish>
            Ingredients Summary: <list of requirements>
            Estimated Cost: <Estimated cost of this dish denoted in U.S. dollars and give dollar sign>
            Estimated Time: <Estimated time of this dish>
            Calorie: <Estimated Calorie of this dish>
            Recipe and Instructions: <>
            Info: <Suggest how does this dish helps with the requirements mentioned if they are mentioned else skip this step>


        
        ```{text}```
        """

        conversation_history.append({"role": "user", "content": prompt_answer})
        response = get_completion(conversation_history)
        conversation_history.append({"role": "assistant", "content": response})
        # Display the response in the desired format
        formatted_response = response.split("\n")
        # Get the image URL using the 'dalle' function
        # Define the regular expression pattern
        pattern = r"Dish Name: (.+)"
        # Use re.findall to find all matches of the pattern
        matches = re.findall(pattern, response)
        print(matches)
        image_url = dalle(matches[0])

        col1, col2 = st.columns(2)

        # Column 1 - Placeholder for some content
        with col1:
            # Display the image
            st.image(image_url, use_column_width=True)

        # Column 2 - Placeholder for the response from the prompt
        with col2:
            for line in formatted_response:
                st.markdown(line)

            # Provide a download link
            # Use st.experimental_singleton to prevent re-run
            ste.download_button("Download recipe!", response, "dish-info.txt")


if __name__ == "__main__":
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
        main()
