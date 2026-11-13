from random import choice
from hangman_pictures import HANGMAN_PICS

input_words = "words.txt"


# načtení seznamu slov (s použitím list comprehension)
def read_words(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = file.readlines()
            words = [line.strip() for line in data]
        if not words:
            print(f"The file {file_path} is empty.")
            return None    
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return None 
    else:
        return words        


# stav hry (s použitím ternárního operátoru)
def show_game_status(missed_guesses_count, guessed_word, missed_letters):
    picture_index = 0 if missed_guesses_count == 0 else missed_guesses_count - 1
    print(HANGMAN_PICS[picture_index])
    print("Missed letters:", ", ".join(missed_letters))
    print(" ".join(guessed_word)) 


# náhodný výběr slova, přes import fce z knihovny
def choose_random_word(words_list):
    secret_word = choice(words_list)      
    return secret_word


# kontrola validity vstupu
def check_validity(guessed_letters, missed_letters):
    while True:
        guessed_letter = input("Guess a letter.") 
        if not guessed_letter.isalpha() or len(guessed_letter) != 1: 
            print("Guess a single letter!")
            continue
        elif guessed_letter in (guessed_letters + missed_letters):
            print("You already guessed this letter. Guess another letter.")
            continue
        else:
            return guessed_letter 


# zprocesování uhodnutého písmena
def process_correct_guess(guessed_letter, secret_word, guessed_letters, guessed_word):
    if guessed_letter in secret_word:
        guessed_letters.append(guessed_letter) 
        for index, letter in enumerate (secret_word):
            if guessed_letter == letter:
                guessed_word[index] = guessed_letter
        return True
    else:
        return False   


# volba, zda znovu spustit vnější cyklus
def play_again():
    while True:
        answer = input("Do you want to play again? (yes or no)")
        if answer == "yes":
            return True      
        elif answer == "no":
            return False 


words_list = read_words(input_words)  
if words_list is not None:               
    # herní cyklus
    while True:
        # náhodný výběr slova, přes import fce z knihovny
        secret_word = choose_random_word(words_list)   
        # vytisknutí aktuálního obrázku spolu s aktuálními políčky na písmena
        missed_guesses_count = 0
        missed_letters = []
        guessed_letters = []
        maximum_wrong_guesses = len(HANGMAN_PICS)
        guessed_word = ["_"]*len(secret_word) 
        while missed_guesses_count <= maximum_wrong_guesses:
            show_game_status(missed_guesses_count, guessed_word, missed_letters)
            guessed_letter = check_validity(guessed_letters, missed_letters)
            if process_correct_guess(guessed_letter, secret_word, guessed_letters, guessed_word):
                if "".join(guessed_word) == secret_word:
                    show_game_status(missed_guesses_count, guessed_word, missed_letters)
                    print("You won the game!")
                    break
            else:
                missed_letters.append(guessed_letter)
                missed_guesses_count += 1
                if missed_guesses_count == maximum_wrong_guesses:
                    show_game_status(missed_guesses_count, guessed_word, missed_letters)
                    print(f"You have run out of guesses! After {len(missed_letters)} missed guesses and {len(guessed_letters)} correct guesses, the word was {secret_word}.")
                    break
        if not play_again(): 
            break

                   

        
                




