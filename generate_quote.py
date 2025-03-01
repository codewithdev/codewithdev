import os
import requests

def fetch_quote():
    url = "https://api.api-ninjas.com/v1/quotes?category=knowledge"
    api_key = os.getenv("API_NINJAS_KEY")
    
    if not api_key:
        print("ERROR: API_NINJAS_KEY environment variable not set")
        return "API key not configured properly."
        
    headers = {
        "X-Api-Key": api_key 
    }
    
    try:
        response = requests.get(url, headers=headers)
        print(f"Response Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Response JSON: {data}")
            
            if isinstance(data, list) and len(data) > 0:
                quote_data = data[0]
                return f"{quote_data['quote']} - {quote_data['author']}"
            else:
                return "No quotes for today."
        else:
            print(f"Error response: {response.text}")
            return "Could not fetch a quote."
    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        return "Error fetching quote."

def update_readme(quote):
    try:
        readme_path = "README.md"
        
        # Check if README file exists
        if not os.path.exists(readme_path):
            print(f"ERROR: {readme_path} not found")
            return False
            
        # Read the current README
        with open(readme_path, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Look for quote marker
        marker = "<!--QUOTE-->"
        if marker not in content:
            print(f"ERROR: Marker '{marker}' not found in README")
            return False
        
        # Replace the quote section
        quote_line = f"{marker}\n> {quote}\n"
        if marker in content:
            # Replace existing quote section with new one
            parts = content.split(marker)
            if len(parts) >= 2:
                # Find the end of the current quote section
                current_section_end = parts[1].find('\n\n')
                if current_section_end != -1:
                    new_content = parts[0] + quote_line + parts[1][current_section_end:]
                else:
                    new_content = parts[0] + quote_line + '\n\n' + parts[1].lstrip()
            else:
                new_content = content.replace(marker, quote_line)
        else:
            new_content = content
        
        # Write the updated content back
        with open(readme_path, "w", encoding="utf-8") as file:
            file.write(new_content)
            
        print("README updated successfully")
        return True
    except Exception as e:
        print(f"Exception updating README: {str(e)}")
        return False

# Main execution
quote = fetch_quote()
print(f"Fetched Quote: {quote}")

success = update_readme(quote)
if not success:
    print("Failed to update README")
    exit(1)  # Fail the GitHub Action
