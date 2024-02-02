import requests
from bs4 import BeautifulSoup


def get_text():
    url = "https://press.oscars.org/news/96th-oscarsr-nominations-announced"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html")
    soup.find_all("p")


def get_nominees():
    pass
