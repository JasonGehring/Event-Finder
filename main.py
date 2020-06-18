import sqlite3
import enger
import eventim

conn = sqlite3.connect('Enger.db')

def createTable():
    c = conn.cursor()

    c.execute('''create table events
    (titel text,
    kurzbeschreibung text,
    link text,
    datum text,
    uhrzeit text,
    veranstalter text,
    ort text,
    kosten text,
    beschreibung text,
    links text)''')

def scrape_eventim():
    citys = [
    'Bünde',
    'Herford',
    'Bielefeld'
    ]

    for i in citys:
        x = "https://www.eventim.de/events/konzerte-1/?cityname=" + i
        y = eventim.event(x)
        #scrapytime mit y

scrape_eventim()
