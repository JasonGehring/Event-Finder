import requests
from bs4 import BeautifulSoup






#bekommt einen link von der event suche und gibt die einzelnen event titel und links wieder
class event:
    def __init__(self, link):
        #holt sich eine webseiten html ( enger event page )
        self.webseite = requests.get(link).text
        self.soup = BeautifulSoup(self.webseite, 'lxml')

        #kleiner workaround results = container für alle events auf der seite
        x = self.soup.find_all(class_='bgsuchmaske')
        results = x[1]

        self.results_amount = int(str(results.h4.text).replace('Suchergebnis (', '').replace(' Veranstaltungen)', ''))
        self.events = results.find_all(style='float:left;')

        self.titel = []
        self.shortDescription = []
        self.links = []

        for event in self.events:
            #link des events
            self.links.append("https://www.enger.de" + str(event.h4.a['href']))


            #titel des events
            self.titel.append(event.h4.a.text)

            #nicht jedes event hat eine kurzbeschreibung
            try :
                self.shortDescription.append(str(event.find(style='width:525px;').text).replace('mehr Informationen', ''))

            #wenn es keine kurzbeschreibug gibt leer printen
            except :
                self.shortDescription.append("")




#bekommt einen link von einem Event und gibt alle wichitgen daten zurück
class eventPage:
    def __init__(self, link):
        #holt sich eine webseiten html ( enger event page )
        self.webseite = requests.get(link).text
        self.soup = BeautifulSoup(self.webseite, 'lxml')

        x = self.soup.find_all(class_='bgsuchmaske')
        results = x[1]

        metanamen = results.find_all(class_='mtp_dl')
        metadaten = results.find_all(class_='mtp_dr')

        self.datum = None
        self.uhrzeit = None
        self.veranstalter = None
        self.ort = None
        self.kosten = None
        try:
            self.description = results.find(class_='mtp_f_text').text
        except:
            self.description = None

        try:
            self.links = results.find(class_='csslink_extern').text
        except:
            self.links = None

        i = -1

        for feld in metanamen:
            i = i+1
            if feld.text == "Datum:":
                self.datum = metadaten[i].text

            elif feld.text == "Uhrzeit:":
                self.uhrzeit = metadaten[i].text

            elif feld.text == "Veranstalter:":
                self.veranstalter = metadaten[i].text

            elif feld.text == "Veranstaltungsort:":
                self.ort = metadaten[i].text

            elif feld.text == "Kosten:":
                self.kosten = metadaten[i].text

            else:
                print("Lustiger Fehler")



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
