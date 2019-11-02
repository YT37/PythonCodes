from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.indiatoday.in/news.html").text
soup = BeautifulSoup(source, "lxml")

print("Here Are Your Top Three News Of The Day:")

for headlines in soup.find_all("h3", class_="news-page-feature"):
    for t in headlines.find_all("a", href=True, text=True):
        head = t.text
        link = t["href"]

        print("\n")
        print(head + ":")
        print(f"https://www.indiatoday.in{link}")

