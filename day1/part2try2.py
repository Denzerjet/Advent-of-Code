def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words

depths = readFile("depths.txt")

increases = 0
place = 0

for i in depths:
    

print(increases)