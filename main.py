import json
import requests
from facebook_scraper import get_posts
from bs4 import BeautifulSoup



def scrape_eventPage(eventPage):
    webseite = requests.get(eventPage).text
    soup = BeautifulSoup(webseite, 'lxml')

    x = soup.find_all(class_='bgsuchmaske')
    results = x[1]

    metanamen = results.find_all(class_='mtp_dl')
    metadaten = results.find_all(class_='mtp_dr')

    for x in metanamen:
        

    datum = y[0].text

    uhrzeit = y[1].text

    veranstalter = y[2].text

    veranstaltungsort = y[3].text

    kosten = y[4].text

    description = results.find(class_='mtp_f_text').text

    links = results.find(class_='csslink_extern').text

    return links

#holt sich eine webseiten html ( enger event page )
webseite = requests.get('https://www.enger.de/Leben-in-Enger/Veranstaltungen/index.php?ModID=11&object=tx%2C1470.316.1&La=1&NavID=1470.476&k_sub=1&ort=393.6&monat=&kat=1.276&va=&vo=&text=').text

#iniziiere suppe
soup = BeautifulSoup(webseite, 'lxml')

#kleiner workaround results = container für alle events auf der seite
x = soup.find_all(class_='bgsuchmaske')
results = x[1]

#scraped results amount
results_amount = int(str(results.h4.text).replace('Suchergebnis (', '').replace(' Veranstaltungen)', ''))

#event liste
events = results.find_all(style='float:left;')

for event in events:

    #titel des events
    titel = event.h4.a.text

    #nicht jedes event hat eine kurzbeschreibung
    try :
        shortDescription = str(event.find(style='width:525px;').text).replace('mehr Informationen', '')

#        print(shortDescription)


    #wenn es keine kurzbeschreibug gibt leer printen
    except :
        print("")

print(scrape_eventPage('https://www.enger.de/Leben-in-Enger/Veranstaltungen/Konzert-Duo-Sing-Your-Soul-Klarinetten-mit-Konzertakkordeon-in-der-Stiftskirche-Enger.php?object=tx,1470.316.1&ModID=11&FID=1470.16310.1&NavID=1470.476&La=1&kat=1.276&ort=393.6'))



#print(results.prettify())

# def search(string, querry):
#     a = string.lower()
#
#     if a.find(querry) >= 1:
#         print("gefunden")
#         print(string.encode("utf-8"))
#
#
# for post in get_posts('zeremonienmeister.dold', pages=2, credentials=['Jasoninator@web.de', 'Gitarre125040708']):
#     try:
#         print(post)
#         search(post['text'], "live")
#     except:
#         print("FEHLER")
