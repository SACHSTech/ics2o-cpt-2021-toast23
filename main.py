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
unit1Q = ["What is the correct sequence of events in computer processing?\nA. input, processing, output, storage\nB. storage, processing, output, input\nC. processing, input, storage, output", "Which of the following statements are true?\nA. Bits are a binary digit consisting of 1 or 0.\nB. Bits correspond with electrical values on/off\nC. All of the above", "How many bits(b) are in a byte(B)?\nA. 5 bits\nB. 8 bits\nC. 10 bits", "How many megabytes(MB) are in a gigabyte(GB)?\nA. 500 MB\nB. 1000 MB\nC. 1024 MB", "Which of the following statements are true?\nA. megahertz(MHz) & gigahertz(GHz) measure download speed\nB. megahertz(MHz) & gigahertz(GHz) measure uploading speed\nC. megahertz(MHz) & gigahertz(GHz) measure processing speed", "What does DPI stand for?\nA. disputes potential index\nB. dots per inch\nC. data processing institute", "What does CPU stand for?\nA. central processing unit\nB. computer processing unit\nC. computing program unit", "What is the purpose of the motherboard?\nA. supply power to the computer\nB. store data for long term use\nC. connect all the components of the computer together", "What does RAM stand for?\nA. random access memory\nB. remaining access memory\nC. random access malfunction", "What is the purpose of the CPU?\nA. store data for short periods of time needed to sustain and run programs\nB. execute commands and compute the basic logic of a computer\nC. render computer graphics", "What is Moore’s law?\nA. the number of transistors in an integrated circuit doubles every 2 years\nB. the number of transistors in an integrated circuit is halved every 2 years\nC. the number of transistors in an integrated circuit will never change", "Which of the following peripheral components is considered an input device?\nA. hard drive\nB. microphone\nC. monitor", "Which of the following peripheral components is considered an output device?\nA. GPU\nB. DVDs\nC. headphones", "Who founded Windows?\nA. Steve Jobs\nB. Bill Gates\nC. Elon Musk", "What is an operating system?\nA. a piece of software that manages a computer’s basic functions\nB. a piece of software that focuses on protecting the computer from viruses\nC. a piece of software that allows users to edit videos", "What is the linux command to print the name of the current working directory?\nA. ls\nB. pwd\nC. mkdir", "What is the linux command to copy a file?\nA. mv\nB. echo\nC. Cp", "Which of the following is a type of multimedia software?\nA. Spotify\nB. Chrome\nC. Audacity", "What is the function of a utility software?\nA. create multimedia\nB. create other softwares\nC. fix problems and maintain the performance of a computer", "What does ISP stand for?\nA. internet service provider\nB. internet service problem\nC. intermediate signal provider", "What does DNS stand for?\nA. dominant naming system\nB. domain name system\nC. deviated nasal septum", "What does WWW stand for?\nA. world wide web\nB. world wide worm\nC. wide worm web", "What does HTTPS stand for?\nA. help transfer protocol secure\nB. hypertext transfer protocol secure\nC. hypertext translate problematic situation", "What is a trojan virus?\nA. malware that spies on you by tracking your online activity\nB. malware that captures every keystroke the user types\nC. malware that misleads people of its true intentions to gain access to their computer", "Which of the following should you do when your computer receives a virus?\nA. Run an antivirus program\nB. Leave it alone\nC. Destroy your computer before attempting any scans."]
unit2Q = ["questions"]

#answer bank
unit1A = ["a", "c", "b", "c", "c", "b", "a", "c", "a", "b", "a", "b", "c", "b", "a", "b", "c", "a", "c", "a", "b", "a", "b", "c", "a"]
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
    #lock user into picking 1, 2
    while True:
        units = input("\nEnter the units you would like: ")
        if units == "1" or units == "2" or units == "12" or units == "21":
            break
        print("\nPlease enter 1 and/or 2.")
    #format quiz based on user input 
    #unit 1
    if units == "1" or units == "11":
        while questionsGiven < 25:
            randomNum = random.randint(0, 24)
            if randomNum in usedNum:
                continue
            usedNum.append(randomNum)
            while True:
                question = input(f"\n{unit1Q[randomNum]}\n").lower()
                if question == "a" or question == "b" or question == "c":
                    break
                print("Enter A, B, or C.\n")
            if question == unit1A[randomNum]:
                score += 1
                print(f"\nCorrect! Your score is {score}/25.")
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
                if question == "a" or question == "b" or question == "c":
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
                if question == "a" or question == "b" or question == "c":
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
                if question == "a" or question == "b" or question == "c":
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
        restart = input("\nWould you like to try again? (yes/no): ").lower()
        if restart == "yes":
            main()
            break
        elif restart == "no":
            print("\nHave a good day!")
            break
        else:
            print("\nPlease type in either yes or no.\n")



#call function
main()
