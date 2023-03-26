import requests

def GetNewWord():
    response = requests.get("https://random-word-api.herokuapp.com/word")
    return response.json()[0]
