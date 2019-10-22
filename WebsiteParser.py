from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("http://coreyms.com").text
soup = BeautifulSoup(source, "lxml")
num = soup.find("div", class_="archive-pagination").text
last = int(num[-15] + num[-14]) + 1

csvFile = open("Article.csv", "w")
csvWriter = csv.writer(csvFile)
csvWriter.writerow(["Heading", "Summary", "Video"])

for i in range(1, last):
    source = requests.get(f"http://coreyms.com/page/{i}").text
    soup = BeautifulSoup(source, "lxml")

    for article in soup.find_all("article"):

        heading = article.h2.a.text
        summary = article.find("div", class_="entry-content").p.text

        try:
            video = "https://youtube.com/watch?v={}".format(
                article.find("iframe", class_="youtube-player")["src"]
                .split("/")[4]
                .split("?")[0]
            )

        except TypeError:
            video = None

        csvWriter.writerow([heading, summary, video])

csvFile.close()
