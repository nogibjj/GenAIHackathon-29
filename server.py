import streamlit as st
from dotenv import load_dotenv
import os
import openai

load_dotenv()

# Set up your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize conversation history as an empty list
conversation_history = []


def get_completion(messages, model="gpt-3.5-turbo-0301"):
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

        
        Only the following output has to be displayed and nothing else before this should be displayed in the output. Make sure all the following is displayed.
        Use the following format and only take this format in the same order as mentioned below, if no instruction is given, assume some healthy dish and proceed.:\
        
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
