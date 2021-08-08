# AHMED IFHAAM
# TP057671
#POST-SUBMISSION
#confirmation of post submission

# RESTRICTIONS
# SCOPE: GLOBAL VARIABLES NOT ALLOWED
# OR ON "GLOBAL" Keyword in Functions ?

# TODO
# checkIn.txt missing case
# non integer for int
# regex for time

from time import sleep
from os import system, name
from abc import ABC, abstractmethod
import string
import re
import os

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
    hour_1 = 4
    hour_2_3 = 2
    hour_4_ = 1

    def __init__(self, record):
        self.checkInTime = int(record['checkInTime'])
        self.checkOutTime = int(record['checkOutTime'])

    def __calculateDuration(self):
        return abs(self.checkOutTime - self.checkInTime)

    def calculateTotalPrice(self):
        time = self.__calculateDuration()
        totalPrice = self.hour_1
        if time > 100:
            totalPrice = totalPrice + self.hour_2_3
        if time > 200:
            totalPrice = totalPrice + self.hour_2_3
        if time > 300:
            totalPrice = totalPrice + ((time - 300) / 100) * self.hour_4_

        return totalPrice


class Car(Vehicle):
    hour_1 = 4
    hour_2_3 = 2
    hour_4_ = 1


class Van(Vehicle):
    hour_1 = 6
    hour_2_3 = 3
    hour_4_ = 2


class Motorbike(Vehicle):
    hour_1 = 2
    hour_2_3 = 1
    hour_4_ = 0


def mainMenu():
    print("Parking Management System\n")
    print("1 : Check In Vehicle")
    print("2 : Check Out Vehicle")
    print("3 : Accounts Information")
    print("4 : Search")
    print("0 :  Exit\n")

    return evaluateChoice(min=0, max=4)


def generateRecordsWithTotal():
    dictList = mightyFileDictionaryToListDictionary("checkOut.txt")
    
    pass

def accountsMenu():
    clear()
    print("1 : View Total Amount for Each Vehicle Type")
    print("2 : Filter all Transactions exceeding RM8")
    # TODO Filter by Custom Amount, Default 8
    print("0 : Back to Main Menu")

    choice = evaluateChoice(min=0, max=2)

    if choice == 1:
        with open("checkOut.txt", 'r') as file:
            for line in file.readlines():
                print(line)
        input("\nPress any key to continue..")
    elif choice == 2:  # no need elif, can use if

        pass
    clear()


def searchMenu():
    clear()
    print("1 : Search for Parking lot via Vehicle Reg No")
    print("2 : Filter Search Vehicles Exceeding 3 hours")
    print("0 : Back to Main Menu")
    # TODO Filter Search by Custom Hour, Default 3

    choice = evaluateChoice(min=0, max=2)
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
            if vehicle[0] != 'C' and vehicle[0] != 'c' and vehicle[0] != 'V' and vehicle[0] != 'v' and vehicle[0] != 'M' and vehicle[0] != 'm':
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
                raise InvalidRegistrationNumberError(
                    "Invalid Registration Number\n")
        except InvalidRegistrationNumberError as error:
            print(error)
        else:
            validated = True
    return regNumber


def verifyCheckInTime() -> int:
    validated = False
    while not validated:
        try:
            inTime = int(
                input("Enter Check-In/Out Time <- [00:00] - [23:59] : "))
            if inTime > 2359 or inTime < 0:
                raise InvalidTimeError(
                    "Error: Enter a number between 0 & 2359\n")
        except InvalidTimeError as error:
            print(error)
        else:
            validated = True
    return inTime


def isFileEmpty(filename: str) -> bool:
    fileDir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    rel_path = filename
    abs_file_path = os.path.join(fileDir, rel_path)
    # removes absolute path errors
    # TODO remove after testing
    # TODO add reference to python doc & so

    with open(abs_file_path, 'r+') as file:  # no file case
        line = file.readline()
        if not line:
            return True
    return False


def assignParkingLot() -> int:
    try:
        if isFileEmpty("checkIn.txt"):
            return 1
        lotList = []
        with open("checkIn.txt", 'r'):
            listDictionary = mightyFileDictionaryToListDictionary("checkIn.txt")
            for line in listDictionary:
                lotList.append(int(line["lot"]))
        #lotList = list(lotList)
        # print(lotList)
        for x in range(1, 21):
            #print("Checking Lot.. ", x)
            lot = x
            if lot not in lotList:
                return lot
        else:
            return -1
    except FileNotFoundError as error:
        print(error, "\nThere was an error creating 'checkIn.txt'")


def mightyFileDictionaryToListDictionary(fileName: str) -> list:
    try:
        lineList: list = []
        with open(fileName, 'r') as file:
            for line in file.readlines():
                lineDict: dict = {}
                line = line[1:(len(line)-2)]
                # -2 to negate \n char in file
                line = line.translate(str.maketrans('', '', string.whitespace))
                # .replace() with timeit() proved 3 times slower
                line = line.replace("'", '')
                pattern = re.compile(r"([\w]+):([A-Za-z0-9-]+)")
                #pattern = re.compile(r"('[\w]+'):([A-Za-z0-9]+|'[A-Za-z0-9]+')")
                # TODO fix '-' in group(2)
                # TODO include re.IGNORECASE flag
                matches = pattern.finditer(line)
                for match in matches:
                    (key, value) = match.group(1), match.group(2)
                    lineDict[key] = value
                lineList.append(lineDict)
    except FileNotFoundError as error:
        print(error, "\nFile name should be 'check(In/Out).txt'")
    return lineList


def vehicleCheckIn():
    clear()
    print("""VEHICLE CHECK-IN MENU
*********************\n""")
    # TODO move assigning first
    parkingLot: int = assignParkingLot()
    if parkingLot == -1:
        print("Warning: ALL LOTS OCCUPIED!")
        return None
    elif parkingLot <= 10:  # TODO DEF FUNCTION
        print("|--> FLOOR : 1 | LOT : ", parkingLot, "\n")
    elif parkingLot > 10:
        print("|--> FLOOR : 2 | LOT : ", parkingLot, "\n")
    vehicle: str = vehicleTypeVerification()
    vehi_RegNo: str = verifyRegistrationNumber()
    checkInTime: int = verifyCheckInTime()
    vehicleDict = {"lot": parkingLot,
                   "registrationNumber": vehi_RegNo,
                   "vehicleType": vehicle,
                   "checkInTime": checkInTime,
                   "checkOutTime": None,
                   }
    if vehicle == 'C':
        pass
    elif vehicle == 'V':
        pass
    elif vehicle == 'M':
        pass
    return vehicleDict


def writeToFile(line: dict):
    with open("checkIn.txt", 'a') as file:
        file.write(str(line)+"\n")


# no need to verify, already verified when registering
def plateNumberExists(plate: str):
    dictList = mightyFileDictionaryToListDictionary("checkIn.txt")
    for dict in dictList:
        if dict['registrationNumber'] == plate:
            return dict
    else:
        return 404


def calculatePrice(record: dict):
    if record['vehicleType'] == 'C':
        recObj = Car(record)
    elif record['vehicleType'] == 'M':
        recObj = Motorbike(record)
    elif record['vehicleType'] == 'V':
        recObj = Van(record)

    price = recObj.calculateTotalPrice()

    return price


def vehicleCheckOut():
    clear()
    print("""VEHICLE CHECK-OUT MENU
*********************\n""")
    vehicleRecord = plateNumberExists(
        str(input("Enter Registration Number : ")))
    if vehicleRecord == 404:
        return 404
    else:
        vehicleRecord['checkOutTime'] = verifyCheckInTime()
    price = calculatePrice(vehicleRecord)

    #copy contents of checkIn.txt into a list
    checkInRecordsList = mightyFileDictionaryToListDictionary("checkIn.txt")

    #delete Record from checkIn.txt
    with open("checkIn.txt", 'w') as file:
        for record in checkInRecordsList:
            if record['registrationNumber'] != vehicleRecord['registrationNumber']:
                file.write(str(record)+"\n")
    #append record to checkOut
    with open("checkOut.txt", 'a') as file:
        file.write(str(vehicleRecord)+"\n")
    

    print("Total Price for Parking : ", price)


while True:
    choice = mainMenu()
    if choice == 1:
        vehicle = vehicleCheckIn()
        if vehicle == None:
            input("\nPress any key to continue..")
        else:
            writeToFile(line=vehicle)
        clear()
    elif choice == 2:
        reply = vehicleCheckOut()
        if reply == 404:
            print("[404] : Vehicle Not Found..")
        input("\nPress any key to continue..")
        clear()
    elif choice == 3:
        accountsMenu()
    elif choice == 4:
        searchMenu()
    elif choice == 0:
        quit()
