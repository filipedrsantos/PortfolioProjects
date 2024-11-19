import numpy as np
import random

import string
import math

# Integer, float

# a = "1"
# print(int(a))
# b= a.isnumeric()
# print(b)
# c = float(a)
# print(c)

# y = 1.3
# print(isinstance(y, int))

# print(float("3.0").is_integer())

# Check "and"

# a = 12
# b = 20
# def tryfun(x):
#     if x > a and x > b:
#         print("ok")
# tryfun(15)

########################################################### Guess a number ##################################################################

def guess(x):
    randnumber = random.randint(1,x)
    # print(randnumber)
    mychoice = input(f"Guess a number between 1 and {x}, or type 'exit' to leave: ")

    run = True
    while (run):

        while mychoice.isnumeric() == False or float(mychoice).is_integer() == False or int(mychoice) < 1 or int(mychoice) > x: #invalid input
            if mychoice == "exit": #Exit
                run = False
                break
            else: 
                mychoice = input(f"Please input an integer number between 1 and {x}, or type 'exit' to leave: ")
            
        if mychoice == "exit": #Exit after invalid input
            run = False
            break

        if int(mychoice) == randnumber:
            print(f"Congrats, {randnumber} was indeed the right number!")
            break
        else:
            # print("Sorry, that is not the number ")
            if int(mychoice) > randnumber:
                mychoice = input("Try to chose a smaller number: ")
            elif int(mychoice) < randnumber:
                mychoice = input("Try to chose a larger number: ")

#guess(10)

# % or

# def guess_v2(x):
#     randnumber = random.randint(1,x)
#     # print(randnumber)
#     mychoice = input(f"Guess a number between 1 and {x}, or type 'exit' to leave: ")

#     while mychoice != randnumber:

#         while mychoice.isnumeric() == False or float(mychoice).is_integer() == False or int(mychoice) < 1 or int(mychoice) > x: #invalid input
#             if mychoice == "exit": #Exit
#                 break
#             else: 
#                 mychoice = input(f"Please input an integer number between 1 and {x}, or type 'exit' to leave: ")
            
#         if mychoice == "exit": #Exit after invalid input
#             break    
        
#         if int(mychoice) == randnumber:
#             print(f"Congrats, {randnumber} was indeed the right number!")
#             break
#         else:
#             if int(mychoice) > randnumber:
#                 mychoice = input("Try to chose a smaller number: ")
#             elif int(mychoice) < randnumber:
#                 mychoice = input("Try to chose a larger number: ")

#guess_v2(10)

################################################### Guess a number in y tries #########################################################

def guess(x):

    randnumber = random.randint(1,x)
    # print(randnumber)
    mytries = input(f"How many tries would you like to try to guess my number? ")
    mychoice = input(f"Guess a number between 1 and {x}, or type 'exit' to leave: ")

    count = 1
    run = True
    while (run):

        while mychoice.isnumeric() == False or float(mychoice).is_integer() == False or int(mychoice) < 1 or int(mychoice) > x: #invalid input
            if mychoice == "exit": #Exit
                run = False
                break
            else: 
                mychoice = input(f"Please input an integer number between 1 and {x}, or type 'exit' to leave: ")
            
        if mychoice == "exit": #Exit after invalid input
            run = False
            break

        if int(mychoice) == randnumber:
            print(f"Congrats, {randnumber} was indeed the right number!")
            break
        else:
            # print("Sorry, that is not the number ")
            if int(mychoice) > randnumber:
                mychoice = input("Try to chose a smaller number: ")
            elif int(mychoice) < randnumber:
                mychoice = input("Try to chose a larger number: ")
        
        count += 1
        # print(count)
        # print(mytries)
        if count == int(mytries):
            print(f"Sorry, you wasted your all of your tries, {randnumber} is the right number!")
            run = False
            break    
            
#guess(10)

################################################### Computer guesses our number ############################################################

def pcguess(x):
    pcnumber =  random.randint(1,x)
    # ournumber = random.randint(1,x)
    ournumber=int(input(f"Choose a number from 1 to {x}: "))
    limmin=0
    limmax=x+1
    while True:
        if pcnumber == ournumber:
            print(f"The pc guessed the number, which is {ournumber}!")
            break
        else:
            # print("The pc failed to guess the correct number ")
            if pcnumber > ournumber:
                print(f"The pc chose a larger number, {pcnumber}")
                limmax = pcnumber
                pcnumber =  random.randint(limmin+1,limmax-1)
            elif pcnumber < ournumber:
                print(f"The pc chose a smaller number, {pcnumber}")
                limmin = pcnumber
                pcnumber =  random.randint(limmin+1,limmax-1)

#pcguess(100)

############################################### Computer guesses our number (faster method) #######################################################

def pcguess(x):
    pcnumber = 50
    # ournumber = random.randint(1,x)
    ournumber=int(input(f"Choose a number from 1 to {x}: "))
    limmin=0
    limmax=x+1
    count = 0
    while True:
        if pcnumber == ournumber:
            print(f"The pc guessed the number, which is {ournumber}!")
            break
        else:
            # print("The pc failed to guess the correct number ")
            if pcnumber > ournumber:
                print(f"The pc chose a larger number, {pcnumber}")
                limmax = pcnumber
                pcnumber = pcnumber - math.floor((pcnumber-limmin)/2)
                
    
            elif pcnumber < ournumber:
                print(f"The pc chose a smaller number, {pcnumber}")
                limmin = pcnumber
                pcnumber = pcnumber + math.floor((limmax-pcnumber)/2)
        count +=1
    print(count+1)

#pcguess(100)

################################################# Computer guesses our number (faster method, get statistics) #######################################

def pcguess(x):
    countall = []
    countnumb = []

    # ournumber = random.randint(1,x)
    for j,i in enumerate(range(1,x+1)):
        ournumber=i
        pcnumber = 50
        limmin=0
        limmax=x+1
        count = 1
        while True:
            if pcnumber == ournumber:
                print(f"The pc guessed the number, which is {ournumber}!")
                break
            else:
                # print("The pc failed to guess the correct number ")
                if pcnumber > ournumber:
                    print(f"The pc chose a larger number, {pcnumber}")
                    limmax = pcnumber
                    pcnumber = pcnumber - math.floor((pcnumber-limmin)/2)
                
    
                elif pcnumber < ournumber:
                    print(f"The pc chose a smaller number, {pcnumber}")
                    limmin = pcnumber
                    pcnumber = pcnumber + math.floor((limmax-pcnumber)/2)
            count +=1
        # print(count)
        countall.append(count)
        countnumb.append(j+1)

    print(countall)
    print(countnumb)

#pcguess(100)

######################################################### Play rock, paper, scissors ############################################################

# rsp= ["rock", "paper", "scissors"]
# a = rsp.count("a")
# print(a==0)

def game():
    rsp= ["rock", "paper", "scissors"]
    result = random.choice(rsp)
    # print(result)

    myplay = input("Choose between rock, paper and scissors (or 1, 2, 3): ")
    if myplay == '1':
        myplay = 'rock'
    elif myplay == '2':
        myplay = 'paper'
    elif myplay == '3':
        myplay = 'scissors'

    while (rsp.count(myplay) == 0) == True:
        myplay = input("Please choose between rock, paper and scissors (or 1, 2, 3): ")

    finalresults = [myplay, result] 
    # print(finalresults) #Both our and oppponent choices

    if myplay == result:
        print(f"Its a draw, the opponent also chose {result}")

    else:
        for i in range(0,len(finalresults)):
            rsp.remove(finalresults[i])
        # print(rsp) # Which one was not chosen
        
        if rsp[0] == "rock":
            if myplay == "scissors":
                print(f"You won, you chose {myplay} and the opponent chose {result}")
            else:
                print(f"You lost, you chose {myplay} and the opponent chose {result}")
        
        elif rsp[0] == "paper":
            if myplay == "rock":
                print(f"You won, you chose {myplay} and the opponent chose {result}")
            else:
                print(f"You lost, you chose {myplay} and the opponent chose {result}")

        elif rsp[0] == "scissors":
            if myplay == "paper":
                print(f"You won, you chose {myplay} and the opponent chose {result}")
            else:
                print(f"You lost, you chose {myplay} and the opponent chose {result}")

# game()

# result = random.choice(rsp)
# print(result)
# print(result == "paper")

# a = ['scissors']
# b = 'scissors'
# print(a[0]==b)

# Remove list from a list
# a = [1,2,3]
# b = [1,3]
# print(a == b)
# for i in range(0,len(b)):
#     a.remove(b[i])
# print(a)

##################################################### Password Generator ####################################################################

# Merge two lists
def merge(list1, list2):
     
    mergedlist = [(p1, p2) for idx1, p1 in enumerate(list1)
    for idx2, p2 in enumerate(list2) if idx1 == idx2]
    return mergedlist

def password():

     # symbols possible to use
    digits = "".join(["0", "1","2", "3","4", "5", "6", "7", "8", "9"]) 
    letters =string.ascii_lowercase
    cletters =string.ascii_uppercase
    symbols = string.punctuation 

    d1 = len(digits)
    d2 = len(letters)
    d3 = len(cletters)
    d4 = len(symbols)

    repetitions = input("Do you want only unique (no duplicate) symbols? press y/n " )
    # number of digits of different kind
    if repetitions == 'n':

        ndigits = input("How many digits: ")
        nletters = input("How many letters: ")
        ncletters = input("How many capital letters: ")
        nsymbols = input("How many special characters: ")
    
    elif repetitions == 'y':

        ndigits = input(f"How many digits (max {d1}): ")
        nletters = input(f"How many letters (max {d2}): ")
        ncletters = input(f"How many capital letters (max {d3}): ")
        nsymbols = input(f"How many special characters (max {d4}): ")

    # testing
    # ndigits = "1"
    # nletters = "2"
    # ncletters = "3"
    # nsymbols = "4"

    lenpass = int(ndigits) + int(nletters) + int(ncletters) + int(nsymbols) # length of password

   

    #allsymbols = digits+letters+cletters+symbols

    # randallsymbols = random.sample(allsymbols, k=len(allsymbols))
    # print(randallsymbols)

    # choose symbols to use (Note that a symbol can be chose more than once, use random.sample if no repetition are desired)
    
    if repetitions == 'n':

        mydigits = random.choices(digits, k=int(ndigits))
        myletters = random.choices(letters, k=int(nletters))
        mycletters = random.choices(cletters, k=int(ncletters))
        mysymbols = random.choices(symbols, k=int(nsymbols))

    elif repetitions == 'y':
    
        mydigits = random.sample(digits, k=int(ndigits))
        myletters = random.sample(letters, k=int(nletters))
        mycletters = random.sample(cletters, k=int(ncletters))
        mysymbols = random.sample(symbols, k=int(nsymbols))

    # print(mydigits)
    # print(myletters)
    # print(mycletters)
    # print(mysymbols)

    # choose the positions for the different kind of symbols
    
    lst = list(range(0,lenpass))
    ranlst = random.sample(lst, k=len(lst))
    # print(ranlst)

    posdigits = ranlst[0:int(ndigits)]
    posletters = ranlst[int(ndigits):int(ndigits)+int(nletters)]
    poscletters = ranlst[int(ndigits)+int(nletters):int(ndigits)+int(nletters)+int(ncletters)]
    possymbols = ranlst[int(ndigits)+int(nletters)+int(ncletters):lenpass]

    # print(posdigits)
    # print(posletters)
    # print(poscletters)
    # print(possymbols)

    # randomly pairing of the symbols chosen with the positions allowed for that kind of symbol
    
    mydigitsr = random.sample(mydigits, k=len(mydigits))
    mylettersr = random.sample(myletters, k=len(myletters))
    myclettersr = random.sample(mycletters, k=len(mycletters))
    mysymbolsr = random.sample(mysymbols, k=len(mysymbols))

    digitschoice = merge(mydigitsr,posdigits)
    letterschoice = merge(mylettersr,posletters)
    cletterschoice = merge(myclettersr,poscletters)
    symbolschoice = merge(mysymbolsr,possymbols)

    # print(digitschoice)
    # print(letterschoice)
    # print(cletterschoice)
    # print(symbolschoice)

    passjoin = digitschoice + letterschoice + cletterschoice + symbolschoice
    # print(passjoin)

    passjoin.sort(key=lambda a: a[1])   
    # print(passjoin)

    passf =[]
    for i in range(len(passjoin)):
        passf.append(passjoin[i][0])
    # print(passf)

    finalpass = ''.join(str(e) for e in passf)
    print(finalpass)

password()

