import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0'}
buende = 'https://www.eventim.de/events/konzerte-1/?cityname=B%C3%BCnde'

class event:
    def __init__(self, link):
        self.webseite = requests.get(link, headers=headers).text
        self.soup = BeautifulSoup(self.webseite, 'lxml')

        self.events = self.soup.find_all('article', class_='listing-container')

        #------ add results amount
        self.titel = []
        self.datum = []
        self.links = []
        self.kosten = []
        self.ort = []

        for i in self.events:

            self.titel.append(str(i.find(class_='listing-headline').text).replace('            ', '').replace('\n       ', ''))

            x = i.find_all(class_='listing-subheadline')

            self.datum.append(str(x[0].span.text).replace('\n', '').replace('                            ', ''))
            self.ort.append(str(x[1].span.span.text))

            self.kosten.append(str(i.find(class_='listing-event-price').text).replace('\n                    ab ', '').replace('\n            ', '').replace('\xa0', ' '))

            self.links.append('https://www.eventim.de' + str(i.find('a', class_='btn')['href']))
