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

# Define the company requirements and the user's resume
company_requirements = "We are looking for a candidate with 2-3 years of experience in AI and ML, proficient in Python, and with experience in data analysis and model deployment."
user_resume = """
Name: James Gossling
Education: BCA, 2020
Experience:
- AI ML Developer at InfoTech (2021-2023)
- Intern at DataCorp (2020-2021)
Skills: Python, TensorFlow, Data Analysis, Model Deployment
"""

# Constructing the interview prompt
prompt = f"""
Company Requirements:
{company_requirements}

User Resume:
{user_resume}

Your role is to conduct an interview with the user based on the given requirements and their resume. Start with easier questions and gradually move to more challenging ones. Ensure the user feels like they are being interviewed by a professor, not an AI. Use the chat history to build upon previous questions and answers. Here is an example of how to structure the interview:

Interviewer: What is your name?
User: Hello Sir, My Name is James Gossling.

Interviewer: So James Gossling, tell me about yourself.
User: I am an AI ML Developer at InfoTech and I ....

Interviewer: So I can see from your resume that you have 2 years of experience in AI and ML using Python. Can you tell me the difference between 'with open' and 'open' file operations in Python?
User: Yes Sir, the open function is used to open a file and returns a file object, which allows you to read from or write to the file. However, when you use open without with, you need to manually close the file using the close method to free up system resources.

Interviewer: Okay, good. So can you tell me why we need a while loop when we already have a for loop?
User: ....

Conduct the interview with a total of at least 15 questions, gradually increasing in difficulty. Make sure to ask questions based on both the company's requirements and the details in the user's resume.

Start the interview now.
"""

response = chat_session.send_message(prompt)

print(response.text)
