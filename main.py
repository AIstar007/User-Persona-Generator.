import sys
import os
from reddit_scraper import extract_posts_comments
from persona_builder import build_persona

def save_persona(username: str, persona: str):
    os.makedirs("output", exist_ok=True)
    output_path = os.path.join("output", f"{username}.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(persona)
    print(f"[+] Persona saved to {output_path}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <reddit_username>")
        return

    username = sys.argv[1]
    print(f"[+] Fetching data for Reddit user: {username}")
    
    data = extract_posts_comments(username)
    if not data["posts"] and not data["comments"]:
        print("[!] No data found for this user.")
        return

    print("[+] Generating user persona using GPT...")
    persona = build_persona(data)
    
    save_persona(username, persona)

if __name__ == "__main__":
    main()