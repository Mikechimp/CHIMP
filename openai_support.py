import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_scan(scan_output):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a cybersecurity assistant."},
            {"role": "user", "content": f"Here is a port scan result:\n{scan_output}\n\nSummarize the findings."}
        ]
    )
    return response['choices'][0]['message']['content']

