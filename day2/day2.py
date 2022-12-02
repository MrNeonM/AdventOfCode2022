### Day 2: Rock Paper Scissors ###

mainList = []
abcList = []
xyzLidt = []
score = 0

with open('./day2/day2_input.txt','r') as f:
    contents = f.read().splitlines()

for line in contents:
    mainList.append(line.split(' '))

## A = Rock, B = Paper, C = Scissors
## X = Rock, Y = Paper, Z = Scissors
for round in mainList:
    elfInput = round[0]
    myInput = round[1]

    # score for picking:
    if myInput == 'X': score += 1
    elif myInput == 'Y': score += 2
    elif myInput == 'Z': score += 3
    
    # win/loss:
    if (((elfInput == 'A') & (myInput == 'X')) | ((elfInput == 'B') & (myInput == 'Y')) | ((elfInput == 'C') & (myInput == 'Z'))): score += 3 # draw
    elif (elfInput == 'A') & (myInput == 'Z'): score += 0 # loss, elfs rock beats my scissors
    elif (elfInput == 'B') & (myInput == 'X'): score += 0 # loss, elfs paper beats my rock
    elif (elfInput == 'C') & (myInput == 'Y'): score += 0 # loss. elfs scissors beats my paper
    elif (elfInput == 'A') & (myInput == 'Y'): score += 6 # win, my paper beats elfs rock
    elif (elfInput == 'B') & (myInput == 'Z'): score += 6 # win, my scissors beats elfs paper
    elif (elfInput == 'C') & (myInput == 'X'): score += 6 # win, my rock beats elfs scissors

print("My final score: ",score)