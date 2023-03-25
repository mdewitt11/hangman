from os import system
from words import GetNewWord
from game_functions import ShowIntroScreen, MainGameLoop, ShowEnding, GetPlayAgain

ShowIntroScreen()
running = True
while running:
    word = GetNewWord()
    [word_is_guessed, number_of_fails] = MainGameLoop(word)
    ShowEnding(word_is_guessed, number_of_fails)
    running = GetPlayAgain()
