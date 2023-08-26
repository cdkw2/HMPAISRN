import requests
from bs4 import BeautifulSoup

url = "https://whoisinspace.com/"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

target_div = soup.find('div', class_='sqs-html-content')
specific_h1 = target_div.find('h1', style='text-align:center;white-space:pre-wrap;')

if specific_h1:
    print(specific_h1.get_text())
else:
    print("Specific h1 element not found.")
