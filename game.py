import cursor
from words import GetNewWord
import game_functions

game_functions.ShowIntroScreen()
running = True
while running:
    cursor.hide()
    word = GetNewWord()
    [word_is_guessed, number_of_fails] = game_functions.MainGameLoop(word)
    game_functions.ShowEnding(word, word_is_guessed, number_of_fails)
    running = game_functions.GetPlayAgain()
    cursor.show()
