# Nutri AI - Duke Generative AI Hackathon Fall 2023

## Project Overview
**Inspiration**
Our Nutri AI is here to reshape the way we approach food. In a world dominated by fast and ready-made meals, our bot becomes your personalized meal planner and recipe generator right on your phone. Whether you're a pregnant woman seeking nutritious options or a budget-conscious gym enthusiast craving diverse and protein-rich dishes, our bot is your all-in-one solution for a healthier and more enjoyable culinary journey.

**What it is**
Currently, the Nutri AI app takes the user's prompt and returns a dish recommended to the user, with nutrition facts, budget, and recipe information. Users can also download responses and log in to the application.
In the future, the Nutri AI app aims to create custom recipes to match your groceries, dietary needs, time, and budget, elevating your daily meals. It also suggests nearby supermarkets for efficient shopping, simplifying meal planning, and promoting healthy choices.


## Running the Application 🧨  
Following are the steps to run the StreamLit Application: 

**1. Create a new conda environment and activate it:** 
```
conda create --name <inser-name> python=3.1
conda activate <inser-name>
```
**2. Install python package requirements:** 
```
pip install -r requirements.txt 
```
**4. Add OpenAI API Key**
```
Rename the env.example file to .env and add your OpenAI API key
```
**5. Run the application**
```
streamlit run About.py --client.showErrorDetails=false
```



## Future Project Scope:

In the next phase of our project, we have ambitious plans to enhance and expand our services to provide a more comprehensive and tailored experience to our users. Here are the key areas we aim to focus on:

**1. Leveraging RAG and Official Documents:** We intend to integrate the RAG (RRetriever-Augmented Generation) model into our platform. Our goal is to utilize this advanced model to train on documents sourced from reputable official websites, such as the US Agriculture Department. This will enable us to provide more accurate and up-to-date information to our users.

**2. Customized Responses with User History:** To create a more personalized and engaging experience, we plan to harness the power of a user's chat history. By analyzing their past interactions with the system, we can offer responses that are finely tuned to their preferences and needs.

**3. Geo-Specific Information:** One of our key objectives is to make the user experience more location-centric. We will incorporate geolocation data to provide users with pertinent local information, including real-time food prices, nearby grocery stores, and restaurant recommendations.

**4. End-to-End Experience:** Our vision is to transform the user journey into a seamless, end-to-end process. This means not only offering assistance with meal planning and recipes but also assisting users in their grocery shopping endeavors. We aim to bridge the gap between planning and cooking, making it a unified and hassle-free experience.

**5. Scaling for Wider Accessibility:** As we seek to broaden our user base, we understand the importance of technical preparedness. To accommodate increased traffic and user demand, we will focus on building a more robust and secure application infrastructure and database. This will ensure that our platform remains accessible, reliable, and scalable as we extend our reach to more people.

In summary, our future project endeavors revolve around enhancing the quality and personalization of our services, catering to specific user needs, and expanding our platform's accessibility. We are committed to delivering a more integral and user-centric experience, all while ensuring our technical infrastructure is ready to scale with the growing demand.
