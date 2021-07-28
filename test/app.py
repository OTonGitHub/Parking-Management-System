import string
import re
import os
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

print(os.stat("test.txt").st_size)
print(os.path.getsize("test.txt"))

# with open("test.txt", 'r') as file:
#     file.seek(0, os.SEEK_END)
#     if file.tell():
#         print("is not Empty")
#         file.seek(0)
#     else:
#         print("File is Empty")


# content = open("test.txt", 'r').read()
# if re.search(r'^\s*$', content):
#     print("isEmpty")

def isFileEmpty(filename) -> bool:
    fileDir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    rel_path = "test.txt"
    abs_file_path = os.path.join(fileDir, rel_path)
        #removes absolute path errors
        #TODO remove after testing

    with open(abs_file_path, 'r') as file:
        line = file.readline()
        print(line[0])
        if line[0] != '{':
            return True
    return False