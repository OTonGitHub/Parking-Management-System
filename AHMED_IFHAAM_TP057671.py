# AHMED IFHAAM
# TP057671

# RESTRICTIONS
# SCOPE: GLOBAL VARIABLES NOT ALLOWED
# OR ON "GLOBAL" Keyword in Functions ?
from time import sleep
from os import system, name
from abc import ABC, abstractmethod
import string
import re

print("OT's CPython")
print("*" * 12, "\n")


def clear():
    _ = system('clear')

# custom-defined Exceptions
class InvalidChoiceError(Exception):
    pass
class InvalidVehicleError(Exception):
    pass
class InvalidRegistrationNumberError(Exception):
    pass
class InvalidTimeError(Exception):
    pass

class Vehicle:
    pass


class Car:
    pass


class Van:
    pass

class Motorbike:
    pass


def mainMenu():
    print("Parking Management System\n")
    print("1 : Check In Vehicle")
    print("2 : Check Out Vehicle")
    print("3 : Accounts Information")
    print("4 : Search")
    print("0 :  Exit\n")

    return evaluateChoice(min=0, max=4)


def accountsMenu():
    clear()
    print("1 : View All Transactions [total]")
    print("2 : Filter all Transactions exceeding RM8")
    # TODO Filter by Custom Amount, Default 8
    print("0 : Back to Main Menu")

    choice = evaluateChoice(min = 0, max = 2)

    if choice == 1:
        with open("test.txt", 'r') as file:
            for line in file.readlines():
                print(line)
        input("\nPress any key to continue..")
    elif choice == 2:#no need elif, can use if
        pass
    clear()


def searchMenu():
    clear()
    print("1 : Search for Parking lot via Vehicle Reg No")
    print("2 : Filter Search Vehicles Exceeding 3 hours")
    print("0 : Back to Main Menu")
    # TODO Filter Search by Custom Hour, Default 3

    choice = evaluateChoice(min = 0, max = 2)
    clear()


def evaluateChoice(min, max):
    validated = False

    while(not validated):
        try:
            choice = int(input("Choice : "))
            if choice > max or choice < min:
                raise InvalidChoiceError(
                    f"Please choose a number between {min} and {max}\n")
        except InvalidChoiceError as Error:
            print(Error)
        else:
            validated = True

    return choice


def vehicleTypeVerification() -> str:
    validated = False

    while(not validated):
        try:
            vehicle = str(input("Vechicle Type (C/V/M) : "))
            if vehicle[0]!='C' and vehicle[0]!='c' and vehicle[0]!='V' and vehicle[0]!='v' and vehicle[0]!='M' and vehicle[0] != 'm':
                raise InvalidVehicleError(
                    f"Please Enter Correct Vehicle Type, [Car, Van, Motorbike]\n")
        except InvalidVehicleError as Error:
            print(Error)
        else:
            validated = True
    return vehicle[0].upper()


def verifyRegistrationNumber() -> str:
    validated = False
    while not validated:
        try:
            regNumber = str(input("Vehicle Registraion Number : "))
            if len(regNumber) == 0 or len(regNumber) > 10:
                raise InvalidRegistrationNumberError("Invalid Registration Number\n")
        except InvalidRegistrationNumberError as error:
                print(error)
        else:
            validated = True
    return regNumber


def verifyCheckInTime() -> int:
    validated = False
    while not validated:
        try:
            inTime = int(input("Enter Check-In Time <- [00:00] - [23:59] : "))
            if inTime > 2359 or inTime < 0:
                raise InvalidTimeError("Error: Enter a number between 0 & 2359\n")
        except InvalidTimeError as error:
            print(error)
        else:
            validated = True
    return inTime

def giveParkingLot() -> int:
    listDictionary = mightyFileDictionaryToListDictionary()
    
    try:
        with open("test.txt", 'r') as file:
            line = file.readline()
    except FileNotFoundError as error:
        print(error,"\nThere was an error creating 'test.txt'")
    return 0

def mightyFileDictionaryToListDictionary() -> list:
    try:
        lineList: list = []
        with open("test.txt", 'r') as file:
            for line in file.readlines():
                lineDict: dict = {}
                line = line[1:(len(line)-2)]
                    #-2 to negate \n char in file
                line = line.translate(str.maketrans('', '', string.whitespace))
                    #.replace() with timeit() proved 3 times slower
                line = line.replace("'", '')
                pattern = re.compile(r"([\w]+):([A-Za-z0-9-]+)")
                    #pattern = re.compile(r"('[\w]+'):([A-Za-z0-9]+|'[A-Za-z0-9]+')")
                    #TODO fix '-' in group(2)
                    #TODO include re.IGNORECASE flag
                matches = pattern.finditer(line)
                for match in matches:
                    (key, value) = match.group(1), match.group(2)
                    lineDict[key] = value
                lineList.append(lineDict)
    except FileNotFoundError as error:
        print(error, "\nFile name should be 'test.txt'")
    return lineList


def vehicleCheckIn() -> dict:
    clear()
    print("""
            VEHICLE CHECK-IN MENU
            *********************\n""")
    vehicle: str = vehicleTypeVerification()
    vehi_RegNo: str = verifyRegistrationNumber()
    checkInTime: int = verifyCheckInTime()
    parkingLot: int = giveParkingLot()
    vehicleDict = {"lot" : parkingLot,
                    "registrationNumber" : vehi_RegNo,
                    "vehicleType" : vehicle,
                    "checkInTime" : checkInTime,
                    "checkOutTime" : None,
    }
    if vehicle == 'C':
        pass
    elif vehicle == 'V':
        pass
    elif vehicle == 'M':
        pass
    return vehicleDict


def writeToFile(line: dict):
    with open("test.txt", 'a') as file:
        file.write(str(line)+"\n")


while True:
    choice = mainMenu()
    if choice == 1:
        vehicle = vehicleCheckIn()
        writeToFile(line = vehicle)
        input("\nPress any key to continue..")
        clear()
    elif choice == 2:
        print("You have chosen option 2")
        print("Press any key to continue..")
        input()
        clear()
    elif choice == 3:
        accountsMenu()
    elif choice == 4:
        searchMenu()
    elif choice == 0:
        quit()
