import requests
import json

def fetch_and_save():
    try:
        # Fetch from ZenQuotes (Python doesn't get blocked!)
        response = requests.get('https://zenquotes.io/api/today')
        data = response.json()
        
        # Save it to a static JSON file
        with open('quote.json', 'w') as f:
            json.dump(data[0], f)
        print("Successfully updated quote.json")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_and_save()