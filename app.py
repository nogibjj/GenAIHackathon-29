import streamlit as st
from dotenv import load_dotenv
import os
import openai

load_dotenv()

# Set up your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize conversation history as an empty list
conversation_history = []


def get_completion(messages, model="gpt-3.5-turbo"):
    """grabs completion"""
    print(messages)
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.1,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


st.set_page_config(layout="wide")
st.title("Figure out a good name")

# Get user input using a text input field
text = st.text_input("Enter your prompt here:")

# Check if the user has entered a prompt
if text:
    # Display the prompt
    st.write(f"You entered: {text}")

    # Perform actions similar to your Flask app
    # need to give a better prompt
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

    conversation_history.append({"role": "user", "content": prompt_answer})
    response = get_completion(conversation_history)
    conversation_history.append({"role": "assistant", "content": response})
    # Display the response in the desired format
    formatted_response = response.split("\n")

    # Create three columns
    col1, col2, col3 = st.columns(3)

    # Column 1 - Placeholder for some content
    with col1:
        st.write("Column 1 Content")
        # You can add any content you want in this column

    # Column 2 - Placeholder for the response from the prompt
    with col2:
        for line in formatted_response:
            st.markdown(line)

    # Column 3 - Placeholder for some content
    with col3:
        st.write("Column 3 Content")
        # You can add any content you want in this column
