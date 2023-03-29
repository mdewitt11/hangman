""" main game functions for hangman game """
from os import system
from subprocess import CompletedProcess, run, PIPE
import re
from time import sleep
from ascii_art import intro_screen, hangman


all_letters: list[str] = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def show_intro_screen() -> None:
    """ shows the hangman title screen """
    system('clear')
    print(intro_screen)
    sleep(3)


def get_user_input() -> str:
    """ gets a single character input from the user"""
    key_press: str = ''
    match: re.Match[str] | None = None
    while not match:
        key_byte: CompletedProcess = run(["./get_key_press.sh"], check=True, stdout=PIPE)
        key_press: str = key_byte.stdout[:1:].decode("utf-8")
        match: re.Match[str] | None = re.search("[A-Za-z]", key_press)
    return key_press


def ContainsChar(array, char) -> bool:
    for c in array:
        if c == char:
            return True
    return False


def IsWordGuessed(word, char_array) -> bool:
    has_character: bool = True
    for c in word:
        has_character = ContainsChar(char_array, c)
        if not has_character:
            break
    return has_character


def GetWordHelper(word, character_list) -> str:
    word_helper: str = ""
    center_space: int = int((38 - len(word) * 2)/2)
    for _ in range(center_space):
        word_helper += " "
    for char in word:
        if ContainsChar(character_list, char):
            word_helper = word_helper + char + " "
        elif char == " ":
            word_helper = word_helper + "  "
        else:
            word_helper = word_helper + "_ "
    return word_helper


def ShowWord(word) -> None:
    word_string: str = GetWordHelper(word, all_letters)
    print(word_string)


def PrintGuessedLetters(guessed_characters) -> None:
    line1: str = "       "
    line2: str = "       "
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


def main_game_loop(word) -> tuple[bool, int]:
    guessed_characters: list[str] = [" "]
    number_of_fails: int = 0
    available_guesses: int = 7
    word_is_guessed: bool = False
    while number_of_fails < available_guesses:
        system('clear')
        print(hangman[number_of_fails])
        word_helper = GetWordHelper(word, guessed_characters)
        print(word_helper)
        PrintGuessedLetters(guessed_characters)
        word_is_guessed = IsWordGuessed(word, guessed_characters)
        if word_is_guessed:
            return (word_is_guessed, number_of_fails)
        user_input: str = get_user_input()
        if not ContainsChar(guessed_characters, user_input):
            guessed_characters.append(user_input)
            if not ContainsChar(word, user_input):
                number_of_fails += 1
        word_helper: str = ""
    return (word_is_guessed, number_of_fails)


def ShowWinnerMessage(word, number_of_fails) -> None:
    system('clear')
    print(hangman[number_of_fails])
    ShowWord(word)
    print()
    print("          Congratulations!!!!")


def ShowLoserMessage(word, number_of_fails) -> None:
    system('clear')
    print(hangman[number_of_fails])
    ShowWord(word)
    print()
    print(" You LOSE... Your a LOSER... ha ha ha")


def ShowEnding(word, word_is_guessed, number_of_fails) -> None:
    if word_is_guessed:
        ShowWinnerMessage(word, number_of_fails)
    else:
        ShowLoserMessage(word, number_of_fails)


def GetPlayAgain() -> bool | None:
    print("           Play again?(y/n)\u001B[0m")
    play_again: str = ''
    while play_again != 'y' and play_again != 'n':
        play_again = get_user_input()
        if play_again == 'y':
            return True
        if play_again == 'n':
            return False
