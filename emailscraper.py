import requests
from bs4 import BeautifulSoup
import re

# Function to scrape a website and extract email addresses
def scrape_website(url):
    try:
        # Send a GET request to the website
        response = requests.get(url)
        response.raise_for_status()  # Check for any errors

        # Create a BeautifulSoup object for parsing the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all email addresses using a regular expression pattern
        email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        emails = set(re.findall(email_pattern, soup.get_text()))

        return emails

    except requests.exceptions.RequestException as e:
        print(f"Error occurred while scraping {url}: {e}")
        return set()

# List of websites to scrape
websites = [
    'https://www.example1.com',
    'https://www.example2.com',
    'https://www.example3.com'
]

# Iterate over the list of websites and scrape email addresses
for website in websites:
    email_addresses = scrape_website(website)

    # Print the email addresses found for each website
    print(f"Email addresses found on {website}:")
    for email in email_addresses:
        print(email)




import requests
from bs4 import BeautifulSoup
import re

class WebsiteScraper:
    def __init__(self):
        self.emails = set()

    def scrape_website(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
            self.emails.update(set(re.findall(email_pattern, soup.get_text())))

        except requests.exceptions.RequestException as e:
            print(f"Error occurred while scraping {url}: {e}")

    def get_emails(self):
        return self.emails


# List of websites to scrape
websites = [
    'https://www.example1.com',
    'https://www.example2.com',
    'https://www.example3.com'
]

# Create an instance of the WebsiteScraper class
scraper = WebsiteScraper()

# Iterate over the list of websites and scrape email addresses
for website in websites:
    scraper.scrape_website(website)

# Get the collected email addresses
email_addresses = scraper.get_emails()

# Print the email addresses found
print("Email addresses found:")
for email in email_addresses:
    print(email)
