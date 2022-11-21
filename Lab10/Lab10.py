from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import time
import re

def imdbFetchFilm(filmID):
    url = "https://www.imdb.com/title/" + filmID + "/fullcredits"
    print("Fetching URL: '"+ url +"'")
    page = urlopen(url)
    html = page.read().decode("utf-8")
    time.sleep(1)

    soup = bs(html,"html.parser")

    castTable = soup.find_all("table","cast_list")[0]
    #print(castTable)
    tdList = castTable.find_all("td", "primary_photo")
    #print(tdList)

    nameIDs = []
    for td in tdList:
        #print("\n"+str(td)+"\n")
        aTag = td.find_all("a")[0]
        href = aTag.get("href")
        nameID = href.strip("/").split("/")[1]
        #print(nameID)
        nameIDs.append(nameID)
    return nameIDs

def imdbFetchPerson(actorID):
    url = "https://www.imdb.com/name/"+ actorID +"/"
    print("Ftching URL: '"+url+"'")
    page = urlopen(url)
    html = page.read().decode("utf-8")
    time.sleep(1)

    soup = bs(html,"html.parser")

    actor_roles = soup.findAll('div', id=re.compile("^actor-tt\d+."))
    actress_roles = soup.findAll('div', id=re.compile("^actress-tt\d+"))
    #print(actor_roles)
    #print(actress_roles)

    acting_roles = actor_roles + actress_roles
    #print(acting_roles)

    film_element_lists = 

def main():
    filmID = "tt9114286"
    actorID = "nm6880265"

    #actor_ids = imdbFetchFilm(filmID)
    film_ids = imdbFetchPerson(actorID)

if __name__=="__main__":
    main()