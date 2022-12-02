### Day 1: Calorie Counting ###

elfList = []
indexList = []
intList = []
currentIndex = 0

# get indexes of input:
with open('./day1/day1_input.txt','r') as f:
    contentIndexes = f.readlines()
    for line in contentIndexes:
        if line == '\n':
            indexList.append(currentIndex)
            currentIndex+=1
        else:
            currentIndex+=1
            continue

# get contents of input:
with open('./day1/day1_input.txt','r') as f:
    contents = f.read().splitlines()

i = 0
for index in indexList:
    if index == indexList[0]: # start of list
        elfList.append(contents[:index])
        i+=1
    elif index == indexList[-1]: # end of list
        elfList.append(contents[index:])
        i+=1
    elif index == indexList[-2]: # 2nd to last
        elfList.append(contents[indexList[i]:indexList[-1]])
        i+=1
    else: # everything in between
        elfList.append(contents[indexList[i-1]:index])
        i+=1

totalElfValue = 0
totalElfValueList = []
for elf in elfList:
    for item in elf:
        try: # get value of singular elf
            itemInt = int(item)
            totalElfValue+=itemInt
        except Exception as e:
            continue
    totalElfValueList.append(totalElfValue)
    totalElfValue = 0
totalElfValueList.sort(reverse=True) # sort list of values in descending order

print("Total Elf Value List (sorted): ",totalElfValueList)
print("Value of top three elves:", (totalElfValueList[0]+totalElfValueList[1]+totalElfValueList[2]))