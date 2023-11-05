# helpers.py

import openai
from streamlit_js_eval import get_geolocation
from streamlit_folium import st_folium
from folium import Map


def miles_to_meter(miles):
    """miles to meter conversion"""
    return miles * 1_609.344


def get_completion(messages, model="gpt-3.5-turbo-0613"):
    """grabs completion"""
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.1,
    )
    return response.choices[0].message["content"]


def generate_prompt_response(text):
    prompt_answer = f"""
        Perform the following actions:
            1 - Look up all memories and summarize the list of ingredients
            2 - Provide the name of a specific healthy dish that is popular in recipe books and list all the ingredients.
            3 - Answer questions in the formation part
            4 - For the `Recipe and Instructions` part, we want the formation to be:

            Using the following format and only respond with this format:
            Ingredients Summary: <list of requirements>
            <find a dish name closely matching the name of the dish>
            Estimated Cost: <Estimated cost of this dish denoted in U.S. dollars>
            Estimated Time: <Estimated time cost of this dish>
            Calorie: <Estimated Calorie of this dish>
            Recipe and Instructions: <>
        ```{text}```
    """

    conversation_history = [{"role": "user", "content": prompt_answer}]
    response = get_completion(conversation_history)
    conversation_history.append({"role": "assistant", "content": response})
    return conversation_history


def display_results_with_location(conversation_history, location):
    formatted_response = response.split("\n")
    image_url = dalle(response)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(image_url, use_column_width=True)

    with col2:
        for line in formatted_response:
            st.markdown(line)

    with col3:
        print(location)
        lat, long = location["coords"]["latitude"], location["coords"]["longitude"]
        lat, lng = get_supermarkets((lat, long))
        st.write("Best Supermarket")
        m = Map(location=[lat, lng], zoom_start=16)
        st_data = st_folium(m, width=725)


def display_results_without_location(conversation_history):
    formatted_response = response.split("\n")
    image_url = dalle(response)

    col1, col2 = st.columns(2)

    with col1:
        st.image(image_url, use_column_width=True)

    with col2:
        for line in formatted_response:
            st.markdown(line)
