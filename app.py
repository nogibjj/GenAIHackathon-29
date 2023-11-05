import streamlit as st
from dotenv import load_dotenv
import os
import openai
import pandas as pd
import googlemaps
from streamlit_js_eval import get_geolocation
import folium
from streamlit_folium import st_folium
import streamlit_ext as ste

load_dotenv()

# Set up your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

if "text" not in st.session_state:
    st.session_state.text = ""

if "location" not in st.session_state:
    st.session_state.location = None


def miles_to_meter(miles):
    """miles to meter conversion"""
    return miles * 1_609.344


def dalle(input_promt):
    """gets an image with openai"""
    response = openai.Image.create(prompt=input_promt, n=1, size="256x256")
    return response["data"][0]["url"]


def get_supermarkets(loc, search_string="supermarket", distance=miles_to_meter(2)):
    """grabs nearest supermakets"""
    business_list = []
    map_client = googlemaps.Client(GOOGLE_API_KEY)
    response = map_client.places_nearby(
        location=loc, keyword=search_string, name="supermarket", radius=distance
    )
    business_list.extend(response.get("results"))

    df = pd.DataFrame(business_list)
    df["url"] = "http://www.google.com/maps/place/?q=place_id:" + df["place_id"]
    df.sort_values("rating", inplace=True, ascending=False)
    lat, lng = (
        df["geometry"][1]["location"]["lat"],
        df["geometry"][1]["location"]["lng"],
    )
    return lat, lng


def get_completion(messages, model="gpt-3.5-turbo-0613"):
    """grabs completion"""
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.1,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


def main():
    """main entry point"""
    st.set_page_config(layout="wide")
    st.title("Figure out a good name")

    # Get user input using a text input field
    st.session_state.text = st.text_input(
        "Enter your prompt here:", st.session_state.text
    )

    st.session_state.location = get_geolocation()

    # Check if the user has entered a prompt
    if st.session_state.text:
        # Display the prompt
        st.write(f"You entered: {st.session_state.text}")

        # Perform actions similar to your Flask app
        # need to give a better prompt
        prompt_answer = f"""
        Perform the following actions:
            1 - Look up all memories and summarize the list of ingredients
            2 - Provide the name of a specific healthy dish that is popular in recipe books and list all the ingredients.
            3 - Answer questions in the formation part
            4 - For the `Recipe and Instructions` part, we want the formation to be:

                Using the following format and only respond with this format:
    
                **Ingredients Summary:** <list of requirements>
                **<find a dish name closely matching the name of the dish>**
                **Estimated Cost:** <Estimated cost of this dish denoted in U.S. dollars>
                **Estimated Time:** <Estimated time cost of this dish>
                **Calorie:** <Estimated Calorie of this dish>
                **Recipe and Instructions:** <>
        ```{st.session_state.text}```
        """

        st.session_state.conversation_history.append(
            {"role": "user", "content": prompt_answer}
        )
        response = get_completion(st.session_state.conversation_history)
        st.session_state.conversation_history.append(
            {"role": "assistant", "content": response}
        )
        # Display the response in the desired format
        formatted_response = response.split("\n")
        # Get the image URL using the 'dalle' function
        image_url = dalle(response)

        # Create three columns
        if st.session_state.location:
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
    main()
