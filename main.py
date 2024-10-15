import requests
from bs4 import BeautifulSoup
import time
import os

URL = "https://interiit-tech.com/problem-statement"
CHECK_INTERVAL = 300  # seconds

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

previous_statements = set()

def send_telegram_message(message):
    """Send a message to a Telegram chat using the bot."""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code != 200:
            print(f"Error sending message: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def check_ps():
    global previous_statements
    try:
        response = requests.get(URL)
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, "html.parser")

        grid = soup.find_all("div", class_="companies-grid")
        if not grid:
            print("No grid found on the page.")
            return
        
        companies = grid[0].find_all("div", class_="company-box")
        
        new_statements = []
        
        for company in companies:
            statement = company.get_text(strip=True)
            if statement and statement not in previous_statements:
                new_statements.append(statement)

        if new_statements:
            message = "New problem statements are available:\n" + "\n".join(new_statements)
            send_telegram_message(message)
            previous_statements.update(new_statements)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    while True:
        check_ps()
        time.sleep(CHECK_INTERVAL)
