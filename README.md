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