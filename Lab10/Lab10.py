from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import time
import re
import random

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

    movieIDs = []
    for role in acting_roles:
        aTag = role.findAll("a")[0]
        href = aTag.get("href")
        movieID = href.strip("/").split("/")[1]
        movieIDs.append(movieID)

    return movieIDs


def imdbfindCommonActors(filmIDs):
    all_actors = []
    for filmID in filmIDs:
        all_actors.append(imdbFetchFilm(filmID))
    
    common_actors = all_actors[0]
    for index in range(len(all_actors)-1):
        common_actors = list(set(common_actors).intersection(all_actors[index+1]))
    
    return common_actors


def imdbFindCommonFilms(actorIDs):
    all_films = []
    for actorID in actorIDs:
        all_films.append(imdbFetchPerson(actorID))

    common_films = all_films[0]
    for index in range(len(all_films)-1):
        common_films = list(set(common_films).intersection(all_films[index+1]))

    return common_films

def main():
    filmID = ["tt0080339","tt0087363","tt0120815","tt12590266","tt0213338"]
    totally_my_favorite_actors = [] 

    all_actor_ids = []
    for film in filmID:
        actor_ids = imdbFetchFilm(film)
        totally_my_favorite_actors.append(random.choice(actor_ids))
        all_actor_ids.append(actor_ids)

    all_film_ids = []
    for actor in totally_my_favorite_actors:
        all_film_ids.append(imdbFetchPerson(actor))

    #print(all_actor_ids)
    #print(all_film_ids)

def extraCredit1():
    iron_Man_Movies = ["tt0371746","tt1228705","tt1300854"]
    common_actors = imdbfindCommonActors(iron_Man_Movies)
    print("Actors that the first 3 Iron man movies have in common.")
    print(common_actors)

def extraCredit2():
    iron_Man_Actors = ['nm0000569', 'nm0000375', 'nm0498278', 'nm0269463', 'nm0079273']
    common_films = imdbFindCommonFilms(iron_Man_Actors)
    print("Films that the lead Iron man actors have in common.")
    print(common_films)


if __name__=="__main__":
    #main()
    extraCredit1()
    extraCredit2()