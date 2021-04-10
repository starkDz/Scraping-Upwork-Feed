import requests
from bs4 import BeautifulSoup
import bs4
from lxml import etree
from datetime import datetime
import time

urlSearch = "https://www.upwork.com/ab/feed/topics/rss?securityToken=e80271d346262cd99dc1d61ac030e2bc0b9bada4b14cc6ad808886d41c797a2c344c2b5804b6d0160a86a3897028e5f4bce4cdcd868f4b95eef7de9da5b0833f&userUid=1380209950211584000&orgUid=1380209950211584001"
url = "https://www.upwork.com/ab/feed/jobs/rss?sort=recency&paging=0%3B10&api_params=1&q=&securityToken=e80271d346262cd99dc1d61ac030e2bc0b9bada4b14cc6ad808886d41c797a2c344c2b5804b6d0160a86a3897028e5f4bce4cdcd868f4b95eef7de9da5b0833f&userUid=1380209950211584000&orgUid=1380209950211584001"
count = 0
now = datetime.now()
print("now =", now)


class scrapUpwork:
    def __init__(self, count, url, i):
        self.count = count
        self.url = url
        self.i = i

    def substractDate(self, dayOne, dayTwo):
        time_delta = dayOne - dayTwo
        total_seconds = time_delta.total_seconds()
        return total_seconds

    def run(self):
        dayOne = datetime.now()
        dayTwo = datetime(2021, 4, 9, 22, 0, 0)
        print(self.substractDate(dayOne, dayTwo))

        try:
            r = requests.get(self.url)
            # file1 = open(str(self.i) + "_RSS.txt", "w")  # write mode
            # file1.write(r.text)
            # file1.close()
            print("The scraping job succeeded: ", len(r.content))
            soup = BeautifulSoup(r.text, "html.parser")
            items = soup.findAll("item")
            for item in items:
                if item.description != None:
                    # findLink = BeautifulSoup(item, "html.parser")
                    # link = findLink.find("link")
                    # print(link)
                    cData = BeautifulSoup(item.text, "html.parser")
                    link = cData.find("link")
                    print(link.text)
                    for strong_tag in cData.find_all("b"):
                        if (
                            strong_tag.text == "Budget"
                            or strong_tag.text == "Hourly Range"
                        ):
                            print(strong_tag.text, strong_tag.next_sibling)
                        if strong_tag.text == "Posted On":
                            print(strong_tag.text, strong_tag.next_sibling)
                            break
                # if (
                #     item.title.text.find("scrap") != -1
                #     or item.title.text.find("excel") != -1
                #     or item.title.text.find("") != -1
                # ):
                print(item.title.text)
                print(
                    "__________________________________________________________________________________________________"
                )
        except Exception as e:
            print("The scraping job failed. See exception: ")
            print(e)


i = 0
print("Starting scraping")
while 1:
    print(
        "************************************** result ("
        + str(i)
        + ") *********************************************"
    )
    hack = scrapUpwork(count, urlSearch, i)
    hack.run()
    print("Finished scraping")
    time.sleep(20)
    i += 1