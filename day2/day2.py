### Day 2: Rock Paper Scissors ###

mainList = []
abcList = []
xyzLidt = []

with open('./day2/day2_input.txt','r') as f:
    contents = f.read().splitlines()

for line in contents:
    mainList.append(line.split(' '))
#--- Part 1: ---#

score = 0

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
    elif (elfInput == 'C') & (myInput == 'Y'): score += 0 # loss, elfs scissors beats my paper
    elif (elfInput == 'A') & (myInput == 'Y'): score += 6 # win, my paper beats elfs rock
    elif (elfInput == 'B') & (myInput == 'Z'): score += 6 # win, my scissors beats elfs paper
    elif (elfInput == 'C') & (myInput == 'X'): score += 6 # win, my rock beats elfs scissors

print("My final score (Part 1): ",score)

#--- Part 2: ---#

score2 = 0

## A = Rock, B = Paper, C = Scissors
## Rock = +1, Paper = +2, Scissors = +3
## X = Loss, Y = Draw, Z = Win
## Loss = +0, Draw = +3, Win = +6

def win(elfInput):
    if elfInput == 'A': return 2 + 6 # 2 for paper, 6 for win
    elif elfInput == 'B': return 3 + 6 # 3 for scissors, 6 for win
    elif elfInput == 'C': return 1 + 6 # 1 for rock, -||-

def loose(elfInput):
    if elfInput == 'A': return 3 + 0 # 3 for scissors, 0 for loss
    elif elfInput == 'B': return 1 + 0 # 1 for rock, -||-
    elif elfInput == 'C': return 2 + 0 # 2 for paper, -||-

def draw(elfInput):
    if elfInput == 'A': return 1 + 3 # 1 for rock, 3 for draw
    elif elfInput == 'B': return 2 + 3 # 2 for paper, -||-
    elif elfInput == 'C': return 3 + 3 # 3 for scissors, -||-

for round in mainList:
    elfInput = round[0]
    desiredOutcome = round[1]

    if desiredOutcome == 'X': score2 += loose(elfInput)
    elif desiredOutcome == 'Y': score2 += draw(elfInput)
    elif desiredOutcome == 'Z': score2 += win(elfInput)

print("My final score (Part 2): ",score2)
