import requests
from bs4 import BeautifulSoup

url = "https://www.aajtak.in/"
response = requests.get(url)
response.raise_for_status()  

soup = BeautifulSoup(response.text, "html.parser")

headlines = []
for item in soup.find_all("h3"):
    text = item.get_text(strip=True)
    if text and text not in headlines:
        headlines.append(text)

with open("headlines.txt", "w", encoding="utf-8") as file:
    for i, headline in enumerate(headlines, 1):
        file.write(f"{i}. {headline}\n")

print(f"\n✅ {len(headlines)} headlines saved to 'headlines.txt'")
