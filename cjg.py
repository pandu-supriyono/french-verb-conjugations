#!/usr/bin/env python

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from unidecode import unidecode

def conjugaison(verb):
    verb_url = 'http://la-conjugaison.nouvelobs.com/du/verbe/' + unidecode(verb) + '.php'

    uClient = uReq(verb_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    temps_tabs = page_soup.findAll("div", {"class":"tempstab"})
    conjugationsList = []

    for conjugations in temps_tabs[:8]:
        title = conjugations.find("h3").text + "\n"
        conjugations = conjugations.find("div", {"class":"tempscorps"})
        for br in conjugations.find_all("br"):
            br.replace_with("\n")
        conjugations = title + conjugations.text
        conjugations = conjugations.splitlines()
        conjugationsList.append(conjugations)

    dict = {conjugations[0]: conjugations[1:] for conjugations in conjugationsList}
    return dict

