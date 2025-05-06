import json
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chunk_list(data, size):
    """Split a list into smaller chunks."""
    for i in range(0, len(data), size):
        yield data[i:i + size]

def summarize_scan(recon_data):
    if not recon_data:
        return "❌ No recon data provided."

    # Separate out SpiderFoot to chunk it
    spiderfoot_entries = recon_data.get("SpiderFoot", [])
    base_data = {k: v for k, v in recon_data.items() if k != "SpiderFoot"}

    all_summaries = []

    # Summarize base recon data (AbuseIPDB + Shodan)
    base_prompt = f"""
You're a cybersecurity analyst. Here's recon data from Shodan and AbuseIPDB.

Summarize open ports, vulnerabilities, CVEs, and threats. Recommend next steps.

Recon Data:
{json.dumps(base_data, indent=2)}
    """

    base_response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You summarize recon data for penetration testing."},
            {"role": "user", "content": base_prompt}
        ],
        temperature=0.4
    )
    all_summaries.append("🧩 Shodan / AbuseIPDB Summary:\n" + base_response.choices[0].message.content)

    # Chunk SpiderFoot data if available
    if spiderfoot_entries:
        chunks = list(chunk_list(spiderfoot_entries, 100))

        for i, chunk in enumerate(chunks, start=1):
            chunk_prompt = f"""
You're a cybersecurity analyst. Here are SpiderFoot results (Chunk {i} of {len(chunks)}).

Summarize only high-confidence or high-risk indicators. Group by IP/domain. Recommend actions.

SpiderFoot Data:
{json.dumps(chunk, indent=2)}
            """

            chunk_response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You summarize recon data for penetration testing."},
                    {"role": "user", "content": chunk_prompt}
                ],
                temperature=0.4
            )

            all_summaries.append(f"🕷️ SpiderFoot Summary — Chunk {i}:\n" + chunk_response.choices[0].message.content)

    return "\n\n".join(all_summaries)
