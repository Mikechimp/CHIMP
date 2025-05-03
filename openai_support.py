from dotenv import load_dotenv
from openai import OpenAI
import os
load_dotenv()

# Load API key from environment variable or .env file (recommended)
# Make sure OPENAI_API_KEY is set before running, or replace below with a string key.
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_scan(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a cybersecurity assistant who summarizes Nmap scan results."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

