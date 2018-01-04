import time # importing the time module.
import random # importing random
import math

def start():
    print("Type simpleInter() to calculate Simple Interest")
    time.sleep(0.3)
    print("Type reverseAText() to find the reverse a sentence or number!")
    time.sleep(0.3)
    print("Type findSumOfDigits() to find the addition of its digits.")
    time.sleep(0.3)
    print("Type lfsum() to find the sum of the first and last digit of a number.")
    time.sleep(0.3)
    print("Type cmds() to view basis commands.")
    time.sleep(0.3)


def simpleInter():
    print("Starting Simple Interest Solver 2.0")
    print()
    time.sleep(2)
    print("Type Principal Amount")
    principal = int(input("$"))
    print("Type the Number of days.")
    days = int(input("[-]"))
    print("Type the rate of interest.")
    rate = int(input("% "))
    time.sleep(1)
    print("Please wait as we give your result:")
    SInterest = principal*rate*days/100
    print()
    digit = "0"
    dollar = "$"
    print("The Simple Interest is:")
    print(dollar, SInterest)
    print()
    time.sleep(0.3)
    print("Again? (type yes)")
    if input("> ") == "yes" :
        simpleInter()
        start()
    else:
        print()

def reverseAText():
    print("Type a two digit number or a word. Watch it reverse!")
    number = input("> ")
    newitem = number[::-1]
    print(newitem)
    time.sleep(2)
    print()
    print("Again? (type yes)")
    if input("> ") == "yes":
        reverseAText()
    else:
        print("")

def cmds():
    print("start()")
    time.sleep(0.3)
    print("reverseANo()")
    time.sleep(0.3)
    print("simpleInter()")
    time.sleep(0.3)
    print("findSumOfDigits()")
    time.sleep(0.3)
    print("lfsum()")
    time.sleep(0.3)
    print("split()")
    time.sleep(0.3)
    print("print()")
    time.sleep(0.3)
    print("input()")
    time.sleep(0.3)
    print("license()")
    time.sleep(0.3)
    print("credits() or credits")
    time.sleep(0.3)
    print("copyright() or copyright")
    time.sleep(0.3)

def findSumOfDigits():
    print("Enter a Number. The digits of the number will add together to get a new number!")
    n=int(input(">"))
    adderandspliter=0
    while(n>0):
        dig=n%10
        adderandspliter=adderandspliter+dig
        n=n//10
    print("The total sum of digits is:",adderandspliter)
    print()
    time.sleep(0.3)
    print("Again? (type yes)")
    if input("> ") == "yes":
        findSumOfDigits()
    else:
        print()

def lfsum():
    print("Enter a number. The first and last digits will add together to for a new number!")
    number = int(input('> '))
    LastDigit = number % 10
    FirstDigit = number // 10 ** int(math.log(number, 10))
    print(FirstDigit + LastDigit)
    print()
    time.sleep(0.3)
    print("Again? (type yes)")
    if input("> ") == "yes":
        lfsum()
    else:
        print()

#COMMANDS RUN HERE
#.tops yretsym ta si redruM
time.sleep(2)
print("A program..")
time.sleep(1)
print("By Upolies.Co")
print()
time.sleep(1)
print("Commands:")
start()
