import math
import time
from collections import namedtuple

#SNAP monthly REQ 
SNAP_REQ = (2608, 3525, 4442, 5358, 6275, 7192)
#minimum amount of hours
HOURS_MIN = 80
#federal req
FEDERAL_REQ = (15960, 21640, 2320, 33000, 38680, 44360, 50040, 55720)
#FEDERAL MIN HOURS
FEDERAL_HOURS_MIN = 80

# snap req
snap = namedtuple("snap", ["income", "hours", "state", "people"])
#Federeal named tuple requirement
fed = namedtuple("fed", ["income", "hours", "people"])


snap = snap(int(input("What is the households yearly income? ")), int(input("What are the hours you have worked? ")), input("Do you live in washington (yes or no)? "), int(input("How many people are in the household? ")))

fed = fed(int(input("What is the households yearly income? ")), int(input("What are the hours you have worked? ")), int(input("How many people are in the household? ")))
#calculate income and return True or False
def income_calc():
    if snap.people <= 6:
        if snap.income <= SNAP_REQ[snap.people - 1]:
            return True
        else:
            return False
    elif snap.people > 6:
        if snap.income <= SNAP_REQ[-1] + (snap.people * 917):
            return True
        else:
            return False



#calculate if they work enough hours
def hours_worked_calc():
    if snap.hours >= HOURS_MIN:
        return True
    else:
        return False
    
#see whether they live in washington or not
def live_in_washington():
    x = str(snap.state)
    if x == "yes":
        return True
    else:
        return False
    
#credits
def credit():
    print("Alex Garcia - Income Calculator")
    print("Duy Tran - Planning, presentaion management")
    print("Diego Hernandez Saldana - ")
    print("Tyler Ivester - ")

#collect all calculations and see if they qualify for snap
def snap_qual():
    if income_calc() == True and hours_worked_calc() == True and live_in_washington() == True:
        print("You qualify")
    else:
        print("you dont qualify")
        print()
#print out why they didnt qualify
        print(f"Qualified income: {income_calc()}")
        print(f"Qualified hours: {hours_worked_calc()}")
        print(f"Live in washington: {live_in_washington()}")
'''
######
######
######
'''
# federal calculator
def fed_calc():
    if fed.people <= 8:
        if fed.income <= SNAP_REQ[snap.people - 1]:
            return True
        else:
            return False
    elif fed.people > 6:
        if fed.income <= SNAP_REQ[-1] + (snap.people * 5680):
            return True
        else:
            return False

#fed hour calc
def fed_hours_worked_calc():
    if fed.hours >= FEDERAL_HOURS_MIN:
        return True
    else:
        return False
#check if they qualify for federal
def federal_qual():
    if fed_calc() == True and fed_hours_worked_calc() == True:
        print("You Qualify")
    else:
        print("you dont qualify")
        print()
        #print why you dont qualify
        print(f"Qualified income: {fed_calc()}")
        print(f"Qualified hours: {fed_hours_worked_calc()}")


#Program
income_calc()
hours_worked_calc()
snap_qual()
#Federal Program
fed_calc()
fed_hours_worked_calc()
federal_qual()