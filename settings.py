import requests

URL = "https://api.freecurrencyapi.com/v1/latest?apikey="
API_KEY = "fca_live_jBZCUGscAeIyZL8QikWn473l5pmcVNhPRpSjn7Ay"


def get_actual_currencies():
    responce = requests.get(URL + API_KEY)
    result = responce.json()
    return result['data']


CURRENCIES = get_actual_currencies()
