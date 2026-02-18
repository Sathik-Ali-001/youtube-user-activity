import json
import os


def load_comments(filename="comments.json"):
    if not os.path.exists(filename):
        print(f" File '{filename}' not found.")
        return []

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data.get("comments", [])


def load_watch_history(filename="watch-history.json"):
    if not os.path.exists(filename):
        print(f"File '{filename}' not found.")
        return []

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data

def show_comments(comments):
    print("\n Your YouTube Comments:\n")
    for i, c in enumerate(comments, 1):
        print(f"{i}. {c.get('comment')}")
        print(f"   Video: {c.get('videoUrl')}")
        print(f"   Time : {c.get('timestamp')}")
        print("-" * 50)


def show_watch_history(history):
    print("\nYour YouTube Watch History:\n")
    count = 0
    for item in history:
        if 'titleUrl' in item and 'Watched' in item.get("title", ""):
            count += 1
            print(f"{count}. {item['title']}")
            print(f"   Link: {item['titleUrl']}")
            print(f"   Time: {item['time']}")
            print("-" * 50)

if __name__ == "__main__":
    
    comments = load_comments("comments.json")
    show_comments(comments)


    history = load_watch_history("watch-history.json")
    show_watch_history(history)