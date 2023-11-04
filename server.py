from flask import Flask, request, jsonify, stream_with_context, Response
import openai
import os
from dotenv import load_dotenv

load_dotenv()
from flask_cors import CORS


# Set up your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
app = Flask(__name__)
cors = CORS(app)


def get_completion(prompt, model="gpt-3.5-turbo"):
    """grabs completion"""
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.1,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


@app.route("/")
def index():
    """initial page"""
    return "Hello from flask"


# get general question
@app.route("/chat", methods=["POST"])
def get_answer():
    # print(request.data)
    # print(type(request.data))
    """grab quick answer frm this"""
    prompt = request.json["question"]
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text


@app.route("/get_dish", methods=["POST"])
def grab_dish():
    """grab answer from prompt"""
    text = request.form["question"]

    prompt_answer = f"""
    Perform the following actions: 
    1 - Look up all memories and summary the list of requirements
    2 - Provide a dish based on the requirements from text
    3 - Answer questions in the formation part
    4 - For the `Recipe and Instructions` part, we want the formation to be: 


    Using the following format:
    Requirements Summary: <list of requirements>
    Dish name: <dish name>
    Estimated Cost: <Estimated cost of this dish>
    Estimated Time: <Estimated time cost of this dish>
    Calorie: <Estimated Calorie of this dish>
    Picture: <Picture of this dish>
    Recipe and Instructions: <>

    ```{text}```
    """
    response = get_completion(prompt_answer)

    return response


@app.route("/get_info", methods=["POST"])
def get_info():
    """get info from user"""
    text = request.form["question"]

    # Our chatbot should
    prompt_questions = f"""
    You are Chef and Nutritionist bot, an automated service that will give suggestions to users about the dishes, \
    You first greet the user and collect information as below. \
    Here are some information we are looking for form the user, so called the expected info:\
    1 - Ingredients at Home \
    2 - Time Constraints \
    3 - Calorie Limitations \
    4 - Dietary Preferences \
    5 - Meal Type \
    6 - Cuisine or Dish Preferences  \
    7 - Allergies \
    8 - Generating Recommendations \
    9 - Recipe and Instructions \
    10 - Adjusting Recommendations \
    11 - Do you want to get more grocery? \

    Perform following actions: \
    1 - Look up all memories and summary the list of requirements \
    2 - Ask the user 3 to 4 questions that matches with the information you want or provide answer if \
        they already provided info. \
        and encourage them to provide any kinds of information?
        
    ```{text}```
    """
    response = get_completion(prompt_questions)

    return response


if __name__ == "__main__":
    app.run(debug=True)
