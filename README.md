📰 Web Scraper for News Headlines
📌 Objective
This Python script scrapes the top news headlines from the BBC News homepage and saves them to a .txt file. It demonstrates basic web scraping using requests and BeautifulSoup.

🛠️ Tools & Technologies
Python 3.x

requests – for sending HTTP requests

beautifulsoup4 – for parsing HTML content

🚀 How It Works
Sends a GET request to the BBC News homepage using requests.

Parses the HTML response using BeautifulSoup.

Extracts all <h3> headline tags.

Filters and writes unique headlines to bbc_headlines.txt.
