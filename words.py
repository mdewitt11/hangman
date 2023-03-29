import requests
from requests.models import Response

def get_new_word() -> str:
    response: Response = requests.get("https://random-word-api.herokuapp.com/word")
    return response.json()[0]
