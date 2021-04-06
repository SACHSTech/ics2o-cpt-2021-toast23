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
unit1Q = ["questions"]
unit2Q = ["questions"]

#answer bank
unit1A = ["answers"]
unit2A = ["answers"]

#main function
def main():
    #variables
    score = 0
    inputError = False
    wrongChoices = 0
   # time.sleep(1.25)
    print("\n********* ICS20 COURSE REVIEW QUIZ *********")
   # time.sleep(1)
    print("\nWhat units would you like to be tested on? You can choose one, two, or all the units. Type the numbers assigned to the units you want. \nExample: understanding computers + programming basics = 12")
   # time.sleep(5)
    print("\n(1) understanding Computers")
   # time.sleep(1)
    print("(2) Programming Basics")
   # time.sleep(1)
    #lock user into picking 1, 2, 3
    while True: 
        units = input("\nEnter the units you would like: ")
        for x in units:
            if x != "1":
                wrongChoices += 1
            if x != "2":
                wrongChoices += 1
            if wrongChoices == 2:
                inputError = True
            wrongChoices = 0
        if inputError == False:
            break
        inputError = False
    #format quiz based on user input 
    if units == "1" or units == "11":
        print("1")
    elif units == "2" or units == "22":
        print("2")
    elif units == "12":
        print("12")
    elif units == "21":
        print("21")     
                
            

#call function
main()
