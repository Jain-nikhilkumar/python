import requests
from bs4 import BeautifulSoup

# Define the URL of the educational content you want to scrape
url = "https://www.geeksforgeeks.org/data-structures/linked-list/9"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract and print the textual content
    textual_content = ""
    for paragraph in soup.find_all('p'):  # Assuming educational content is in <p> tags
        textual_content += paragraph.text + "\n"
    
    # Print the extracted content
    print(textual_content)

else:
    print("Failed to fetch content from the URL.")

# Close the HTTP session
response.close()
