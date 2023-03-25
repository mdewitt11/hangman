import random

words = [
    "a red car", 
    "steam train", 
    "superman", 
    "bay of pigs", 
    "meet your maker", 
    "fainting goats",
    "bars of iron",
    "barns",
    "colorado",
    "boston",
    "chew cude",
    "new",
    "spuper new",
    "brand",
    "volocano",
    "raspberry",
    "guitar",
    "fireball",
    "man of steel",
    "brothers in arms",
    "linux"
    "piano bench",
    "crouching tiger",
    "bible",
    "traditional latin mass",
    "rocking chair",
    "picture frame",
    "piano bench",
    "cello bow",
    "fiddler"
]

def GetNewWord():
    return words[random.randrange(0, len(words))]
