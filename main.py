import requests
from bs4 import BeautifulSoup

url = "https://whoisinspace.com/"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


div_elements = soup.find_all('div', class_='sqs-block-content')


excluded_keywords = ['Stay', 'Subscribe', 'Follow', 'Connect']
names = []

def contains_keyword(name):
    return any(keyword.lower() in name.lower() for keyword in excluded_keywords)

for div in div_elements:
    h2_element = div.find('h2')
    if h2_element:
        name = h2_element.get_text().strip()
        if name and not contains_keyword(name):
            names.append(name)

print(names)
