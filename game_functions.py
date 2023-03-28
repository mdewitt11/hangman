from os import system
from subprocess import run, PIPE
from time import sleep
from ascii_art import intro_screen, hangman
import re


all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ShowIntroScreen():
    system('clear')
    print(intro_screen)
    sleep(3)


def GetUserInput():
    key_press = ''
    match = None
    while not match:
        key_byte = run(["./get_key_press.sh"], check=True, stdout=PIPE)
        key_press = key_byte.stdout[:1:].decode("utf-8")
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


def GetWordHelper(word, character_list):
    word_helper = ""
    center_space = int((38 - len(word) * 2)/2)
    for s in range(center_space):
        word_helper += " "
    for char in word:
        if ContainsChar(character_list, char):
            word_helper = word_helper + char + " "
        elif char == " ":
            word_helper = word_helper + "  "
        else:
            word_helper = word_helper + "_ "
    return word_helper


def ShowWord(word):
    word_string = GetWordHelper(word, all_letters)
    print(word_string)


def PrintGuessedLetters(guessed_characters):
    line1 = "       "
    line2 = "       "
    for l1 in range(0, 13):
        if ContainsChar(guessed_characters, all_letters[l1]):
            line1 += "\u001B[38;5;240m" + all_letters[l1] + " \u001B[38;5;255m"
        else:
            line1 += all_letters[l1] + " "
    for l2 in range(13, 26):
        if ContainsChar(guessed_characters, all_letters[l2]):
            line2 += "\u001B[38;5;240m" + all_letters[l2] + " \u001B[38;5;255m"
        else:
            line2 += all_letters[l2] + " "
    print()
    print(line1)
    print(line2)


def MainGameLoop(word):
    guessed_characters = [" "]
    number_of_fails = 0
    available_guesses = 7
    while number_of_fails < available_guesses:
        system('clear')
        print(hangman[number_of_fails])
        word_helper = GetWordHelper(word, guessed_characters)
        print(word_helper)
        PrintGuessedLetters(guessed_characters)
        word_is_guessed = IsWordGuessed(word, guessed_characters)
        if word_is_guessed:
            return [word_is_guessed, number_of_fails]
        user_input = GetUserInput()
        if not ContainsChar(guessed_characters, user_input):
            guessed_characters.append(user_input)
            if not ContainsChar(word, user_input):
                number_of_fails += 1
        word_helper = ""
    return [word_is_guessed, number_of_fails]


def ShowWinnerMessage(word, number_of_fails):
    system('clear')
    print(hangman[number_of_fails])
    ShowWord(word)
    print()
    print("          Congratulations!!!!")


def ShowLoserMessage(word, number_of_fails):
    system('clear')
    print(hangman[number_of_fails])
    ShowWord(word)
    print()
    print(" You LOSE... Your a LOSER... ha ha ha")


def ShowEnding(word, word_is_guessed, number_of_fails):
    if word_is_guessed:
        ShowWinnerMessage(word, number_of_fails)
    else:
        ShowLoserMessage(word, number_of_fails)


def GetPlayAgain():
    print("           Play again?(y/n)\u001B[0m")
    play_again = ''
    while play_again != 'y' and play_again != 'n':
        play_again = GetUserInput()
        if play_again == 'y':
            return True
        if play_again == 'n':
            return False
