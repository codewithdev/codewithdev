import os
import requests

def fetch_quote():
    url = "https://api.api-ninjas.com/v1/quotes?category=knowledge"
    api_key = os.getenv("API_NINJAS_KEY")
    headers = {
        "X-Api-Key": api_key 
    }
    response = requests.get(url, headers=headers)
    print(f"Response Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list) and len(data) > 0:
            quote_data = data[0]
            return f"{quote_data['quote']} - {quote_data['author']}"
        else:
            return "No quotes for today."
    else:
        return "Could not fetch a quote."

quote = fetch_quote()
print(f"Fetched Quote: {quote}")

# Update the README file with the new quote
with open("README.md", "r") as file:
    lines = file.readlines()

with open("README.md", "w") as file:
    for line in lines:
        if line.strip() == "<!--QUOTE-->":
            file.write(f"> {quote}\n\n")
        else:
            file.write(line)
