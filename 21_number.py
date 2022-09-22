
import os
import time
import random
liste = []
def gamestart():
    print("If you want to start First type > F")
    print("Otherwise you'll start Second for this type > S")
    opt = input("> ")
    if opt.upper() == "F":
        game1()
    elif opt.upper() == "S":
        game2()
    else:
        os.system("CLS")
        print("Please type a valid option.")
        gamestart()

def play_again():
    print("Wanna Try Again? Y or N")
    inp = input("> ")
    if inp.upper() == "Y":
        os.system("CLS")
        print("The Game is starting again...")
        liste.clear()
        gamestart()
    elif inp.upper() == "N":
        print("Çıkış Yapılıyor...")
        time.sleep(2)
        exit()           
    else: 
        print("You didn't choose a correct option!")

def lose():
    print("\\UNFORTUNATELY!!!")
    print("You did LOSE the game :( ")
    play_again()
  
def win():
    print("\n\nCONGRATULATIONS!!!")
    print("You did WIN the game :)")
    play_again()

def check_the_list():
    if liste[0] != 1:
        return False
    for i in range(len(liste)-1):
        if liste[i+1] - liste[i] != 1:
            return False       
    return True

def computer1_turn(numb):
    numb_of_entries = 4 - numb
    for i in range(numb_of_entries):
        liste.append(liste[-1] + 1)

def computer2_turn(check_iterations):
    numb_of_entries = 0
    if check_iterations == 1:
        numb_of_entries = random.randint(1,3)
        for i in range(numb_of_entries):
            liste.append(i + 1)
    else:    
        check_number = liste[-1] % 4
        if check_number == 0:
            numb_of_entries = random.randint(1,3)
        else:
            numb_of_entries = 4 - check_number    
        for i in range(numb_of_entries):
            liste.append(liste[-1] + 1)        

def game1():
    last_number = 0
    print("You're starting!!!")
    while True:
        if last_number == 20:
            lose()
        print("How many number do you want to entry?")
        numb_of_entries_of_person = int(input("> "))
        if not  (numb_of_entries_of_person > 0 and numb_of_entries_of_person < 4):
            print("You are disqualified for entrying inappropriate number.")
            lose()
        print("\nEnter the numbers")
        for i in range(numb_of_entries_of_person):
            numbs = int(input("> "))
            liste.append(numbs)
        if not check_the_list():
            print("You are disqualified for entrying inappropriate number.")
            lose()
        last_number = liste[-1]
        if last_number == 20:
            win()
        print("\nComputer's turn...\n")
        time.sleep(1.5)
        computer1_turn(numb_of_entries_of_person)
        print("the view of list after computer")
        print(f"{liste}\n")
        last_number = liste[-1]
        print("Your Turn...\n")

def game2():
    last_number = 0
    i = 1
    print("Computer's starting!!!")
    while True:
        if last_number == 20:
            win()
        elif last_number > 20:
            lose()
        print("Computer's Turn...")
        time.sleep(2)    
        computer2_turn(i)
        last_number = liste[-1]
        if last_number == 20:
            lose()
        elif last_number > 20:
            win()
        print("the view of list after computer")
        print(f"{liste}\n")
        print("\nYour's Turn!!!\n")    
        print("How many number do you want to entry?")
        numb_of_entries_of_person = int(input("> "))
        if not  (numb_of_entries_of_person > 0 and numb_of_entries_of_person < 4):
            print("You are disqualified for entrying inappropriate number.")
            lose()
        print("\nEnter the numbers")
        for j in range(numb_of_entries_of_person):
            numbs = int(input("> "))
            liste.append(numbs)
        if not check_the_list():
            print("You are disqualified for entrying inappropriate number.")
            lose()    
        last_number = liste[-1]
        i = i + 1

gamestart()

                 