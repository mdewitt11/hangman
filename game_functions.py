from os import system
from time import sleep
from ascii_art import intro_screen, hangman

def ShowIntroScreen():
    system('clear')
    print(intro_screen)
    sleep(3)

def get_user_input():
    user_input = ""
    while len(user_input) != 1:
        user_input = input("Guess a letter:\n>>")
        if len(user_input) != 1:
            print("You must input ONE letter!!!")
    return user_input

def contains_char(array, char):
    for c in array:
        if c == char:
            return True
    return False

def is_word_guessed(word, char_array):
    hasCharacter = True
    for c in word:
        hasCharacter = contains_char(char_array, c)
        if not hasCharacter:
            break
    return hasCharacter

def GetWordHelper(word, guessed_characters):
    word_helper = ""
    for char in word:
        if contains_char(guessed_characters, char):
            word_helper = word_helper + char + " "
        elif char == " ":
            word_helper = word_helper + "  "
        else:
            word_helper = word_helper + "_ "
    return word_helper
    
def MainGameLoop(word):
    guessed_characters = [" "]
    number_of_fails = 0
    available_guesses = 7
    while number_of_fails < available_guesses:
        system('clear')
        print(hangman[number_of_fails]) 
        word_helper = GetWordHelper(word, guessed_characters) 
        print(word_helper)
        word_is_guessed = is_word_guessed(word, guessed_characters)
        if word_is_guessed:
           return [word_is_guessed, number_of_fails]
        user_input = get_user_input()
        if contains_char(word, user_input):
            guessed_characters.append(user_input)
        else:
            number_of_fails += 1
        word_helper = ""
    return [word_is_guessed, number_of_fails]

def ShowWinnerMessage(number_of_fails):
    system('clear')
    print(hangman[number_of_fails]) 
    print("Congratulations!!!!")
    
def ShowLoserMessage(number_of_fails):
    system('clear')
    print(hangman[number_of_fails]) 
    print("You LOSE... Your a LOSER... ha ha ha")

def ShowEnding(word_is_guessed, number_of_fails):
    if word_is_guessed:
        ShowWinnerMessage(number_of_fails)
    else:
        ShowLoserMessage(number_of_fails)

def GetPlayAgain():
    play_again = input("Play again?(yes)\n>> ")
    if play_again != "yes":
        return False
    return True
