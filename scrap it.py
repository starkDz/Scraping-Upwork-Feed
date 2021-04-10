import requests
from bs4 import BeautifulSoup

url = "https://fr.wikipedia.org/wiki/Liste_des_pays_par_population"
response = requests.get(url)
pays = []
Liste_des_pays_par_population = []
if response.ok:
    soup = BeautifulSoup(response.text, "html.parser")
    tds = soup.findAll("td")
    for td in tds:
        link = td.find("img")
        if link != None:
            pays.append(td)
    for pay in pays:
        a = pay.findAll("a")
        for item in a:
            thisItem = item.find("img")
            if thisItem == None and item.find("span") == None:
                Liste_des_pays_par_population.append(item)
    [print(pays) for pays in Liste_des_pays_par_population]
    links = []
    for pays in Liste_des_pays_par_population:
        links.append(pays["href"])
    print(len(Liste_des_pays_par_population))
    print(links)
    capitals = []
    for link in links:
        print("https://fr.wikipedia.org" + link)
        response = requests.get("https://fr.wikipedia.org" + link)
        if response.ok:
            soup = BeautifulSoup(response.text, "html.parser")
            trs = soup.findAll("tr")
            for tr in trs:
                item = tr.find("th")
                if item != None:
                    itemA = item.find("a")
                    if itemA != None and itemA.text == "Capitale":
                        # print(itemA.text)
                        capitals.append(tr)
    data = []
    for capitale in capitals:
        td = capitale.find("td")
        item = td.find("a")
        data.append(td.text)

    [print(capitale) for capitale in data]
