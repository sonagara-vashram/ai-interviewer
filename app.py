import os
import streamlit as st
import google.generativeai as genai

# Configure Google Generative AI API
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

generation_config = {
    "temperature": 0.1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]

system_prompt = """
Assume you are a 10 years of experience in python developer. Your role is to analyze python scripts.
"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    safety_settings=safety_settings,
    generation_config=generation_config,
    system_instruction=system_prompt
)

chat_session = model.start_chat()

# Step 1: Generate a beginner level Python task
task_prompt = """
Generate a random basic level Python task suitable for beginners.
"""
task_response = chat_session.send_message(task_prompt)
beginner_task = task_response.text

# Streamlit UI
st.title("Beginner Python Task Analyzer")
st.write(f"**Your Task:** {beginner_task}")

# User input for their solution
st.write("### Step 2: Provide your solution to the task")
user_code = st.text_area("Write your solution here:", height=200)

# When the user clicks the button, proceed to analyze the script
if st.button("Analyze My Solution"):
    if not user_code.strip():
        analyze_prompt = f"""
        If the user has not provided any script or code, then you should write the entire code for the task.
        Write the whole task in this format:
        ### Task: {beginner_task}
        ### Code: write full code here.
        """
    else:
        analyze_prompt = f"""
        I need to analyze this beginner-level Python task and identify the mistakes in it. If there are any mistakes, provide the corrected code.
        Here is the script:
        {user_code}
        
        """
    
    response = chat_session.send_message(analyze_prompt)
    st.write("### Analysis Result")
    st.write(response.text)

