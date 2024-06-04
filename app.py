import os
import PyPDF2
import google.generativeai as genai

# Configure the Generative AI with your API key
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Define the generation configuration and safety settings
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

# Define the system prompt
system_prompt = """
You have 20 years of experience in conducting interviews.
You will be given some resumes and our requirements.
Based on the given requirements, you need to interview the user.
The user should not feel that you are an AI.
They should feel as if a professor is conducting an online interview.
"""

# Define a function to extract text from the PDF using PyPDF2
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extractText()
    return text

# Extract the resume text from the PDF
pdf_path = "path/to/your/resume.pdf"
resume_text = extract_text_from_pdf(pdf_path)

# Create the generative model and start the chat session
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    safety_settings=safety_settings,
    generation_config=generation_config,
    system_instruction=system_prompt
)

chat_session = model.start_chat()

# Define the prompt with the extracted resume text
prompt = f"""
Here is the candidate's resume:
{resume_text}

Please conduct an interview based on this resume and the following requirements:
- Requirement 1
- Requirement 2
- Requirement 3
"""

# Send the prompt to the chat session
response = chat_session.send_message(prompt)

# Print the response
print(response.text)
