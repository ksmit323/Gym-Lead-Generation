import requests
from bs4 import BeautifulSoup
import json

# Add your Hunter.io API key here
HUNTER_API_KEY = 'e37ccd82ad62f6b4bd6b9e0a2e2a4351c61d0f88'

url = 'https://www.google.com/search?q=gyms+in+hanoi'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

results = soup.find_all('div', {'class': 'dbg0pd'})

gyms = []

for r in results:

    try:
        name = r.find('div', {'class': 'dbg0pd'}).text.strip()
        address = r.find('div', {'class': 'BNeawe s3v9rd AP7Wnd'}).text.strip()
        rating = r.find('span', {'class': 'LGOjhe'}).text.strip()
        gyms.append({'name': name, 'address': address, 'rating': rating})
    except:
        pass

# Use Hunter.io API to find email addresses
for gym in gyms:
    domain = gym['address'].split(',')[1].strip()
    url = f'https://api.hunter.io/v2/domain-search?domain={domain}&api_key={HUNTER_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        if data['data']['emails']:
            email = data['data']['emails'][0]['value']
            gym['email'] = email

print(gyms)
