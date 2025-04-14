import json
import random

def load_quotes():
    with open("assets/quotes.json", "r") as file:
        quotes = json.load(file)
    return quotes

def get_random_quote():
    quotes = load_quotes()
    return random.choice(quotes)
