# This is a Hangman Game.
import random
import os

# this list holds some words which randomly we can pick.
words = ["ümitcan","dilara","kalem","bilgisayar","dizüstü","masa","ayakkabı","salon","resim","fare"]
# this list holds the letters which is guessed by the player.
letters_of_player_guessed = []
# this is main function where the game starts.
def game_start():
    # the number of chances the player has.
    chance = 6
    print("The Game Is Starting...")
    print("The Word Is Selected...")
    word = random.choice(words)
    print(word)
    while True:
        check_the_status = 0
        print("Guess a letter")
        letter = input("> ")
        if check_the_letter2(letter):
            continue

        if check_the_letter(letter,word):
            os.system("cls")
            print("Your Guess Is Correct.\n\n")
            check_the_status = show_current_status(word)
            draw_Hangman(chance)
        else:
            os.system("cls")
            chance -= 1
            print("Your Guess Is Incorrect.")
            print(f"You Have {chance} chances to find out the word.\n\n")
            check_the_status = show_current_status(word)
            draw_Hangman(chance)

        if check_the_status == len(word):
            win()
        elif chance == 0:
            lose()

# this function takes a letter and a word as parameter which is entered by the player and 
# checks whether the letter is in that word or not. after that returns the result.
def check_the_letter(letter,word):
    if letter in word:
        letters_of_player_guessed.append(letter)
        return True
    else:
        return False
# this function takes a letter as a parameter which is entered by the player and
# checks whether it is entered before or not. after that returns the result.
def check_the_letter2(letter):
    if letter in letters_of_player_guessed:
        print("\nYou're Already Guessed That Letter.\n")
        return True
    return False
# this function shows us what status are we in    
def show_current_status(word):
    check_the_game_status = 0
    for i in range(len(word)):
        if word[i] in letters_of_player_guessed:
            print(word[i],end=" ")
            check_the_game_status += 1
        else: 
            print("_",end=" ")
    print("\n")
    return check_the_game_status

def draw_Hangman(chance):
    if chance == 5:
        print("|-----\n"
              "|    |\n" 
              "|    0\n"
              "|\n"    
              "|\n"    
              "|\n"   
              "|\n")
    elif chance == 4:
        print("|-----\n"
              "|    |\n" 
              "|    |\n"
              "|    0\n" 
              "|\n"    
              "|\n"   
              "|\n")
    elif chance == 3:
        print("|-----\n"
              "|    |\n" 
              "|    0\n" 
              "|   /|\ \n"
              "|\n"    
              "|\n"   
              "|\n")
    elif chance == 2:
        print("|-----\n"
              "|    |\n" 
              "|    0\n" 
              "|   /|\ \n"
              "|    | \n"    
              "|\n"   
              "|\n")
    elif chance == 1:
        print("|-----\n"
              "|    |\n" 
              "|    0\n" 
              "|   /|\ \n"
              "|    | \n"    
              "|   / \n"   
              "|\n")
    elif chance == 0:
        print("|-----\n"
              "|    |\n" 
              "|    0\n" 
              "|   /|\ \n"
              "|    | \n"    
              "|   / \ \n"   
              "|\n")

def win():
    print("\nCongratulations!!! You won the Game.")
    exit()

def lose():
    print("\nUnfortunately!!! You lost the Game.")
    exit()
# if I want to add play again section to the game. it's available here.
def play_again():
    letters_of_player_guessed.clear()
    os.system("CLS")
    game_start()
game_start()