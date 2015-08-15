import requests
import json
import pprint
import string

netrunnerdb_URL = "http://netrunnerdb.com/api/cards/"

def getCards(URL):
    cards = requests.get(URL)
    r =  cards.json()
    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(r)
    return r

def get_card_IDs(card_data):
    for card in card_data:
        yield card["code"]

def get_data_and_destiny(card_data):
    for card in card_data:
        if card["setname"].lower() == "data and destiny":
            yield card["code"]

def get_universe_of_tomorrow(card_data):
    for card in card_data:
        if card["setname"].lower() == "the universe of tomorrow":
            yield card["code"]


if __name__ == "__main__":

    cards = getCards(netrunnerdb_URL)
    s = get_card_IDs(cards)

    # for card in cards:
    #     print card["title"], card["setname"], card["code"]
