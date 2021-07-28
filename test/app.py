import string
import re
try:
    lineList: list = []
    with open("test.txt", 'r') as file:
        for line in file.readlines():
            lineDict: dict = {}
            # line = file.readline()
            # print(line)

            line = line[1:(len(line)-2)]
                #-2 to negate \n char in file
            line = line.translate(str.maketrans('', '', string.whitespace))
                #.replace() with timeit() proved 3 times slower
            line = line.replace("'", '')
            pattern = re.compile(r"([\w]+):([A-Za-z0-9-]+)")
                #TODO fix - in group(2) 
            #pattern = re.compile(r"('[\w]+'):([A-Za-z0-9]+|'[A-Za-z0-9]+')")
                #TODO include re.IGNORECASE flag
            matches = pattern.finditer(line)
            #print(line)
            for match in matches:
                (key, value) = match.group(1), match.group(2)
                lineDict[key] = value
            
            lineList.append(lineDict)


            # for  piece in line:
            #     pass
            # for line in file:
            #     (key, value) = line.split(',')
            #     lineDict[int(key)] = value
            # print(lineDict)
            # print(type(lineDict))
except FileNotFoundError as error:
    print(error,"\nFile name should be 'test.txt'")

# print("\n*******DICTIONARY********\n")
# x = 0
# for dictionary in lineList:
#         print(dictionary)


for line in lineList:
    print(line['checkInTime'])

