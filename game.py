import cursor
from words import get_new_word
from game_functions import show_intro_screen, main_game_loop
from game_functions import ShowEnding, GetPlayAgain 

show_intro_screen()
RUNNING = True

while RUNNING:
    cursor.hide()
    word: str = get_new_word()
    [word_is_guessed, number_of_fails] = main_game_loop(word)
    ShowEnding(word, word_is_guessed, number_of_fails)
    RUNNING = GetPlayAgain()
    cursor.show()
