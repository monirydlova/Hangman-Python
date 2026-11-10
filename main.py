input_words = "words.txt"
from random import choice
from hangman_pictures import HANGMAN_PICS

# načtení seznamu slov
def read_words(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = file.readlines()
            words = []
            for line in data:
                word = line.strip()
                words.append(word)
                
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return None 
    else:
        return words

words_list = read_words(input_words) 

# stav hry
def show_game_status(count_round, guessed_word):
    if count_round == 0:
        print(HANGMAN_PICS[count_round])
    elif count_round > 0:
        print(HANGMAN_PICS[count_round-1])
    print("Missed letters:", ", ".join(missed_letters))
    print(" ".join(guessed_word))

# náhodný výběr slova, přes import fce z knihovny
def random_choice_word(words_list):
    word_choosed = choice(words_list)      
    return word_choosed

# volba, zda znovu spustit vnější cyklus:
def play_again():
    while True:
        choice = input("Do you want to play again? (yes or no)")
        if choice == "yes":
            return True      
        elif choice == "no":
            return False
        
# herní cyklus
while True:
# náhodný výběr slova, přes import fce z knihovny
    word_choosed = random_choice_word(words_list)   
# vytisknout aktuální obrázek obrázek spolu s aktuálními políčky na písmena
    count_round = 0
    missed_letters = []
    guessed_letters = []
    maximum_wrong_guesses = len(HANGMAN_PICS)
    guessed_word = ["_"]*len(word_choosed) 
       
    while count_round <= maximum_wrong_guesses:
        show_game_status(count_round, guessed_word)
        guessed_letter = input("Guess a letter.") 

        if not guessed_letter.isalpha() or len(guessed_letter) != 1: 
            print("Guess a single letter!")
            continue
        
        elif guessed_letter in (guessed_letters + missed_letters):
            print("You already guessed this letter. Guess another letter.")
            continue

        elif guessed_letter in word_choosed:
            guessed_letters.append(guessed_letter) 
            for index, letter in enumerate (word_choosed):
                if guessed_letter == letter:
                    guessed_word[index] = guessed_letter

            if "".join(guessed_word) == word_choosed:
                show_game_status(count_round, guessed_word)
                print("You won the game!")
                break
        else:
            missed_letters.append(guessed_letter)
            count_round += 1
            if count_round == maximum_wrong_guesses:
                show_game_status(count_round, guessed_word)
                print(f"You have run out of guesses! After {len(missed_letters)} missed guesses and {len(guessed_letters)} correct guesses, the word was {word_choosed}.")
                break
    if not play_again(): 
        break
    
             
                        
            

        
                




