"""
-------------------------------------------------------------------------------
Name:   main.py
Purpose:  Multiple choice quiz on ICS20 course material
 
Author: Yao.T
 
Created:  26/03/2021
------------------------------------------------------------------------------
"""

#import modules
import random 
import time 

#question bank
unit1Q = ["What is the sequence of events in computer processing?\nA. input, processing, output, storage\nB. storage, processing, output, input\nC. processing, input, storage, output", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
unit2Q = ["questions"]

#answer bank
unit1A = ["a", "y"]
unit2A = ["answers"]

#main function
def main():
    #variables 
    questionsGiven = 0
    usedNum = []
    score = 0
   # time.sleep(1.25)
    print("\n********* ICS20 COURSE REVIEW QUIZ *********")
   # time.sleep(1)
    print("\nWhat units would you like to be tested on? You can choose one, two, or all the units. Type the numbers assigned to the units you want. \nExample: understanding computers + programming basics = 12")
   # time.sleep(5)
    print("\n(1) Understanding Computers")
   # time.sleep(1)
    print("(2) Programming Basics")
   # time.sleep(1)
    #lock user into picking 1, 2, 
    while True:
        units = input("\nEnter the units you would like: ")
        if units == "1" or units == "2" or units == "12" or units == "21":
            break
        print("\nPlease enter 1 and/or 2.\n")
    #format quiz based on user input 
    #unit 1
    if units == "1" or units == "11":
        while questionsGiven <= 25:
            randomNum = random.randint(0, 1)
            if randomNum in usedNum:
                continue
            usedNum.append(randomNum)
            while True:
                question = input(unit1Q[randomNum]).lower()
                if question == "a" or question == "b" or "question" == "c":
                    break
                print("\nEnter A, B, or C.\n")
            if question == unit1A[randomNum]:
                score += 1
                print(f"Correct! Your score is {score}/25.")
                questionsGiven += 1
            else:
                print(f"Incorrect! The answer is {unit1A[randomNum]}. Your score is {score}/25.")
                questionsGiven += 1      
    #unit 2
    elif units == "2" or units == "22":
        while questionsGiven <= 25:
            randomNum = random.randint(0, 1)
            if randomNum in usedNum:
                continue
            usedNum.append(randomNum)
            while True:
                question = input(unit2Q[randomNum]).lower()
                if question == "a" or question == "b" or "question" == "c":
                    break 
                print("\nEnter A, B, or C.\n")
            if question == unit2A[randomNum]:
                score += 1
                print(f"Correct! Your score is {score}/25.")
                questionsGiven += 1
            else:
                print(f"Incorrect! The answer is {unit2A[randomNum]}. Your score is {score}/25.")
                questionsGiven += 1
    #unit 1 and 2 
    elif units == "12" or units == "21":
        while questionsGiven <= 13:
            randomNum = random.randint(0, 1)
            if randomNum in usedNum:
                continue
            usedNum.append(randomNum)
            while True:
                question = input(unit1Q[randomNum]).lower()
                if question == "a" or question == "b" or "question" == "c":
                    break
                print("\nEnter A, B, or C.\n")
            if question == unit1A[randomNum]:
                score += 1
                print(f"Correct! Your score is {score}/25.")
                questionsGiven += 1
            else:
                print(f"Incorrect! The answer is {unit1A[randomNum]}. Your score is {score}/25.")
                questionsGiven += 1
        usedNum.clear()
        while questionsGiven <= 12:
            randomNum = random.randint(0, 1)
            if randomNum in usedNum:
                continue
            usedNum.append(randomNum)
            while True:
                question = input(unit2Q[randomNum]).lower()
                if question == "a" or question == "b" or "question" == "c":
                    break
                print("\nEnter A, B, or C.\n")
            if question == unit2A[randomNum]:
                score += 1
                print(f"Correct! Your score is {score}/25.")
                questionsGiven += 1
            else:
                print(f"Incorrect! The answer is {unit2A[randomNum]}. Your score is {score}/25.")
                questionsGiven += 1            
    #prompt user if they want to do the quiz again   
    while True:    
        restart = input("Would you like to try again? (yes/no): ").lower()
        if restart == "yes":
            main()
            break
        elif restart == "no":
            print("Have a good day!")
            break
        else:
            print("\nPlease type in either yes or no.\n")



#call function
main()
