import requests
from bs4 import BeautifulSoup
import csv

def fetch_page(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return None

def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = []
    for article in soup.select("h2"):
        title = article.get_text(strip=True)
        items.append({"title": title})
    return items

def save_to_csv(data, filename='output.csv'):
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)