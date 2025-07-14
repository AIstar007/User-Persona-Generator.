import requests
import time
from typing import List, Dict

def fetch_reddit_json(url: str) -> Dict:
    headers = {'User-Agent': 'RedditPersonaBot/0.1'}
    response = requests.get(url + ".json", headers=headers)
    time.sleep(1)  # polite pause
    if response.status_code == 200:
        return response.json()
    return {}

def extract_posts_comments(username: str) -> Dict[str, List[Dict]]:
    base_url = f"https://www.reddit.com/user/{username}"
    posts = fetch_reddit_json(base_url + "/submitted")
    comments = fetch_reddit_json(base_url + "/comments")

    def parse_data(data):
        items = []
        if 'data' in data and 'children' in data['data']:
            for child in data['data']['children']:
                c = child['data']
                items.append({
                    'body': c.get('selftext', '') or c.get('body', ''),
                    'url': 'https://www.reddit.com' + c.get('permalink', '')
                })
        return items

    return {
        'posts': parse_data(posts),
        'comments': parse_data(comments)
    }