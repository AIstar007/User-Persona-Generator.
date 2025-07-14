import requests
from typing import List, Dict

def build_persona(data: Dict[str, List[Dict]]) -> str:
    combined_text = "\n\n".join([
        f"{item['body']}\n(Source: {item['url']})"
        for item in data['posts'] + data['comments']
        if item['body'].strip() != ""
    ])

    prompt = f"""
You are an expert in analyzing online discussions. Based on the Reddit posts and comments below, generate a user persona. Include:
1. Interests
2. Beliefs or Opinions
3. Writing Style
4. Personality Traits
5. Any other relevant insights

For each trait, cite specific posts or comments using the provided URLs.

Reddit Data:
{combined_text}
"""

    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    })

    return response.json().get("response", "[Error generating response]")