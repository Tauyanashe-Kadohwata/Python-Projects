import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

headlines = soup.find_all("h3")
for i, headline in enumerate(headlines[:10]):
    print(f"{i+1}. {headline.text.strip()}")
