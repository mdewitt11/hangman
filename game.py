import cursor
from words import GetNewWord
from game_functions import ShowIntroScreen, MainGameLoop, ShowEnding, GetPlayAgain

ShowIntroScreen()
running = True
while running:
    cursor.hide() 
    word = GetNewWord()
    [word_is_guessed, number_of_fails] = MainGameLoop(word)
    ShowEnding(word, word_is_guessed, number_of_fails)
    running = GetPlayAgain()
    cursor.show()
