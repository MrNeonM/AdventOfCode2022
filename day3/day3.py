### Day 3: Rucksack Reorganization ###

rucksackList = []
compartementListTemp = []
compartementList = []
priority = 0

with open('./day3/day3_input.txt','r') as f:
    contents = f.read().splitlines()

for rucksack in contents:
    compartementListTemp.append(rucksack[:len(rucksack)//2])
    compartementListTemp.append(rucksack[len(rucksack)//2:])

i = 0
i1 = 2
for compartement in compartementListTemp:
    compartementList.append(compartementListTemp[i:i1])
    i += 2
    i1 += 2



print(compartementList)
print(len(compartementList))
