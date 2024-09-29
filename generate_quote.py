import os
import requests

def fetch_quote():
    url = "https://api.api-ninjas.com/v1/quotes?category=knowledge"
    api_key = os.getenv("API_NINJAS_KEY") 
    headers = {
        "X-Api-Key": api_key 
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return f"{data['content']} - {data['author']}"
    else:
        return "Could not fetch a quote."

quote = fetch_quote()

# Update the README file with the new quote
with open("README.md", "r") as file:
    lines = file.readlines()

with open("README.md", "w") as file:
    for line in lines:
        if line.strip() == "<!--QUOTE-->":
            file.write(f"> {quote}\n\n")
        else:
            file.write(line)
