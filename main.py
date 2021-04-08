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
unit2Q = ["What variable data type is used when working with letters?\nA. integer\nB. string\nC. float", "What data value do boolean variables use?\nA. numbers\nB. letters\nC. true and false", "What is the symbol used to represent multiplication?\nA. *\nB. **\nC. x", "What is the symbol used to represent modulus (remainder)?\nA. %\nB. **\nC. /", "What is wrong with the following naming practice: 9inningscore\nA. variable name starts with a digit\nB. variable name lacks underscores between words\nC. all of the above", "Which of the following will print “hello world”?\nA. print hello world\nB. print(“hello world)\nC. print(“hello world”)", "What will the following code output?\nprint(“two” + 2)\nA. two2\nB. error\nC. “two” + 2", "What will the following code output?\nx = “10”\nprint(type(x))\nA. 10\nB. <class ‘int’>\nC. <class ‘str’>", "What will the following code output?\nprint(10 - 5)\nA. 5\nB. 10 - 5\nC. error", "What will the following code output?\nprint(“13” + “37”)\nA. “13” + “37”\nB. 1337\nC. 50", "What is the correct order of operations (highest to lowest priority)?\nA. +, ==, /, **\nB. **, /, +, ==\nC. **, +, ==, /", "What will the following code output?\n number = input(“Enter a number: “)\nprint(type(number))\nA. <class ‘int’> \nB. type(number)\nC. <class ‘str’>", "What will the following code output?\nnumber = float(input(“Enter a number: “)\nprint(type(number))\nA. <class ‘float’>\nB. <class ‘str’>\nC. <class ‘int’>", "What will the following code output?\nprint(“1 + 1 = “ + str(2))\nA. 1 + 1 = str(2)\nB. 1 + 1 = 2\nC. error", "The purpose of the following code is to print “hello world” twice. What is wrong with the following code?\nprint(“hello world”)\n#print(“hello world”)\nA. the second print statement is ignored due to #\nB. the string should be surrounded by single quotes, not double\nC. there is nothing wrong with the following code", "What is a syntax error?\nA. an error where the program contains code that does not follow the rules of the python language\nB. an error that produces an unexpected result\nC. an error that occurs during execution when the program attempts to carry out an impossible task", "What is the purpose of an Else statement?\nA. check for multiple conditions\nB. execute a block of code if all conditions are false\nC. none of the above", "What is the main difference between a While and a For loop?\nA. while loops go on forever\nB. for loops run until a condition is met\nC. while loops run until a condition is met", "What will the following code output?\nfor x in range(0, 5):\nprint(x)\nA. 0, 1, 2, 3, 4, 5\nB. 0, 1, 2, 3, 4\nC. 1, 2, 3, 4", "What will the following code output?\nmyList = [“a”, “b”, “c”]\nprint(myList[3])\nA. c\nB. nothing\nC. error", "What number is the first element in a sequence indexed at?\nA. 0\nB. 1\nC. none of the above", "What shape represents conditions in a flow chart?\nA. diamond\nB. square\nC. parallelogram", "What is the output of 9 % 3?\nA. 3\nB. 0\nC. 27", "What is the output of 2 ** 4?\nA. 16\nB. 0.5\nC. 8", "What does the following code output?\nfor x in “code”:\n   print(x)\nA. 1, 2, 3, 4\nB. code\nC. c,o,d,e"]

#answer bank
unit1A = ["a", "c", "b", "c", "c", "b", "a", "c", "a", "b", "a", "b", "c", "b", "a", "b", "c", "a", "c", "a", "b", "a", "b", "c", "a"]
unit2A = ["b", "c", "a", "a", "c", "c", "b", "c", "a", "b", "b", "c", "a", "b", "a", "a", "b", "c", "b", "c", "a", "a", "b", "a", "c"]

#main function
def main():
    #variables 
    questionsGiven = 0
    usedNum = []
    score = 0
    time.sleep(1.25)
    print("\n********* ICS20 COURSE REVIEW QUIZ *********")
    time.sleep(1)
    print("\nWhat units would you like to be tested on? You can choose one, two, or all the units. Type the numbers assigned to the units you want. \nExample: understanding computers + programming basics and control structures = 12")
    time.sleep(2.5)
    print("\n(1) Understanding Computers")
    time.sleep(1)
    print("(2) Programming Basics and Control Structures")
    time.sleep(1)
    #lock user into picking 1, 2
    while True:
        units = input("\nEnter the units you would like: ")
        if units == "1" or units == "2" or units == "12" or units == "21":
            break
        time.sleep(1)
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
                time.sleep(1)
                question = input(f"\n{unit1Q[randomNum]}\n").lower()
                if question == "a" or question == "b" or question == "c":
                    break
                time.sleep(1)
                print("Enter A, B, or C.\n")
            if question == unit1A[randomNum]:
                score += 1
                time.sleep(1)
                print("\nCorrect!")
                questionsGiven += 1
            else:
                time.sleep(1)
                print(f"\nIncorrect! The answer is {unit1A[randomNum]}.")
                questionsGiven += 1      
    #unit 2
    elif units == "2" or units == "22":
        while questionsGiven < 25:
            randomNum = random.randint(0, 24)
            if randomNum in usedNum:
                continue
            usedNum.append(randomNum)
            while True:
                time.sleep(1)
                question = input(f"\n{unit2Q[randomNum]}\n").lower()
                if question == "a" or question == "b" or question == "c":
                    break 
                time.sleep(1)
                print("Enter A, B, or C.\n")
            if question == unit2A[randomNum]:
                score += 1
                time.sleep(1)
                print("\nCorrect!")
                questionsGiven += 1
            else:
                time.sleep(1)
                print(f"\nIncorrect! The answer is {unit2A[randomNum]}.")
                questionsGiven += 1
    #unit 1 and 2 
    elif units == "12" or units == "21":
        while questionsGiven < 13:
            randomNum = random.randint(0, 24)
            if randomNum in usedNum:
                continue
            usedNum.append(randomNum)
            while True:
                time.sleep(1)
                question = input(f"\n{unit1Q[randomNum]}\n").lower()
                if question == "a" or question == "b" or question == "c":
                    break
                time.sleep(1)
                print("\nEnter A, B, or C.\n")
            if question == unit1A[randomNum]:
                score += 1
                time.sleep(1)
                print("\nCorrect!")
                questionsGiven += 1
            else:
                time.sleep(1)
                print(f"\nIncorrect! The answer is {unit1A[randomNum]}.")
                questionsGiven += 1
        usedNum.clear()
        questionsGiven = 0
        while questionsGiven < 12:
            randomNum = random.randint(0, 24)
            if randomNum in usedNum:
                continue
            usedNum.append(randomNum)
            while True:
                time.sleep(1)
                question = input(f"\n{unit2Q[randomNum]}\n").lower()
                if question == "a" or question == "b" or question == "c":
                    break
                time.sleep(1)
                print("\nEnter A, B, or C.\n")
            if question == unit2A[randomNum]:
                score += 1
                time.sleep(1)
                print("\nCorrect!")
                questionsGiven += 1
            else:
                time.sleep(1)
                print(f"\nIncorrect! The answer is {unit2A[randomNum]}.")
                questionsGiven += 1            
    #print score
    time.sleep(1.5)
    print(f"\n\nYou got {score}/25!")
    if score >= 20:
        time.sleep(1)
        print("\nGood job! You're an expert in computers and programming!")
    elif score < 20 and score > 16:
        time.sleep(1)
        print("\nGood job! You have room for improvement!")
    elif score <= 16:
        time.sleep(1)
        print("\nYikes. Please review the lessons again.")
    #prompt user if they want to do the quiz again   
    while True:    
        time.sleep(1)
        restart = input("\n\nWould you like to try again? (yes/no): ").lower()
        if restart == "yes":
            main()
            break
        elif restart == "no":
            time.sleep(1)
            print("\nHave a good day!")
            break
        else:
            time.sleep(1)
            print("\nPlease type in either yes or no.\n")

#call function
main()
