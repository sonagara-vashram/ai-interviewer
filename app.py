import os
import google.generativeai as genai

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
You have 20 years of experience in conducting interviews.
You will be given some resumes and our requirements.
Based on the given requirements, you need to interview the user.
The user should not feel that you are an AI.
They should feel as if a professor is conducting an online interview.
"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    safety_settings=safety_settings,
    generation_config=generation_config,
    system_instruction=system_prompt
)

chat_session = model.start_chat()

prompt = f"""
"""
response = chat_session.send_message(prompt)

print(response.text)