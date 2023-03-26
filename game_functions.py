from os import system  
from subprocess import run, PIPE
from time import sleep
from ascii_art import intro_screen, hangman
import keyboard
import re

def ShowIntroScreen():
    system('clear')
    print(intro_screen)
    sleep(3)

def GetUserInput():
    key_press = ''
    match = None
    while match == None:
        key_press = run(["./get_key_press.sh"], check=True, stdout=PIPE).stdout[:1:].decode("utf-8")
        match = re.search("[A-Za-z]", key_press)
    return key_press

def ContainsChar(array, char):
    for c in array:
        if c == char:
            return True
    return False

def IsWordGuessed(word, char_array):
    has_character = True
    for c in word:
        has_character = ContainsChar(char_array, c)
        if not has_character:
            break
    return has_character

def GetWordHelper(word, guessed_characters): 
    word_helper = ""
    for char in word:
        if ContainsChar(guessed_characters, char):
            word_helper = word_helper + char + " "
        elif char == " ":
            word_helper = word_helper + "  "
        else:
            word_helper = word_helper + "_ "
    return word_helper

def ShowWord(word):
    word_string = ''
    for char in word:
        word_string += char + " "
    print(word_string)

def MainGameLoop(word):
    guessed_characters = [" "]
    number_of_fails = 0
    available_guesses = 7
    while number_of_fails < available_guesses:
        system('clear')
        print(hangman[number_of_fails]) 
        word_helper = GetWordHelper(word, guessed_characters) 
        print(word_helper)
        word_is_guessed = IsWordGuessed(word, guessed_characters)
        if word_is_guessed:
           return [word_is_guessed, number_of_fails]
        user_input = GetUserInput()
        if ContainsChar(word, user_input):
            guessed_characters.append(user_input)
        else:
            number_of_fails += 1
        word_helper = ""
    return [word_is_guessed, number_of_fails]

def ShowWinnerMessage(word, number_of_fails):
    system('clear')
    print(hangman[number_of_fails]) 
    ShowWord(word)
    print("Congratulations!!!!")
    
def ShowLoserMessage(word, number_of_fails):
    system('clear')
    print(hangman[number_of_fails]) 
    ShowWord(word)
    print("You LOSE... Your a LOSER... ha ha ha")

def ShowEnding(word, word_is_guessed, number_of_fails):
    if word_is_guessed:
        ShowWinnerMessage(word, number_of_fails)
    else:
        ShowLoserMessage(word, number_of_fails)

def GetPlayAgain():
    print("Play again?(y/n)")
    play_again = ''
    while play_again != 'y' and play_again != 'n':
        play_again = GetUserInput()
        if play_again == 'y':
            return True
        if play_again == 'n':
            return False
