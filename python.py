import math
from collections import namedtuple

#SNAP monthly REQ 
SNAP_REQ = 1200
HOURS_MIN = 80
# snap req
snap = namedtuple("snap", ["income", "hours", "state"])

snap = snap(int(input("What is the households yearly income? ")), int(input("What are the hours you have worked? ")), input("Do you live in washington (yes or no)? "))
#calculate income and return True or False
def income_calc():
    if snap.income >= SNAP_REQ:
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
            


def snap_qual():
    if income_calc() == True and hours_worked_calc() == True and live_in_washington() == True:
        print("You qualify")
    else:
        print("you dont qualify")

#Program
income_calc()
hours_worked_calc()
snap_qual()