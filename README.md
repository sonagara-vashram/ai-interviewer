
# AI-Powered Interview Bot

This project is an AI-powered interview bot that uses Google Generative AI to conduct interviews based on a candidate's resume. It is designed to create a natural conversational experience where the AI interviewer mimics a professor conducting an online interview.

## Features
- Extracts text from a PDF resume
- Conducts interviews based on predefined requirements
- Mimics human-like conversational flow
- Enforces safety settings to avoid inappropriate content

## Requirements

To run this project, you'll need the following libraries installed:

- `PyPDF2`
- `google-generativeai`
- `os` (standard Python library)

These can be installed using the `requirements.txt` file.

## Installation

### Clone the repository

```bash
git clone https://github.com/sonagara-vashram/ai-interviewer.git
cd ai-interview-bot
```

### Install dependencies

First, make sure you have Python 3.7+ installed. Then, install the required libraries:

```bash
pip install -r requirements.txt
```

The `requirements.txt` should include the following:

```txt
PyPDF2
google-generativeai
```

### Setup API Key

This project uses Google Generative AI. You will need to configure the API key as an environment variable:

```bash
export GOOGLE_API_KEY="your-google-api-key"
```

Make sure to replace `"your-google-api-key"` with your actual API key.

## Usage

Once you have set up everything, you can run the project by following these steps:

1. **Add your resume**: 
   - Place the candidate's resume as a PDF file in the project folder and update the `pdf_path` variable in the code with the correct file path.

2. **Run the script**: 
   - Execute the Python script using the command:

```bash
python interview_bot.py
```

3. **Receive the interview questions**: 
   - The AI will start the interview based on the candidate’s resume and predefined requirements.
