import math

def closestPowerOfTwo(a):
    powersOfTwo = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
    dist = a
    close = 2
    power = 0
    finalPower = 0
    for p in powersOfTwo:
        power = power + 1
        if (dist > abs(a - p)):
            close = p
            finalPower = power
            dist = abs(a - p)
    return (close, finalPower)

def numOfDERounds(a):
    numOfRounds = 3
    powerStuff = closestPowerOfTwo(a)
    numOfRounds = numOfRounds + ((2*powerStuff[1])-2)
    if (a > powerStuff[0]):
        numOfRounds = numOfRounds + 1
    nextPower = powerStuff[0]*2
    dist = nextPower - powerStuff[0]
    if ((a - powerStuff[0]) > (dist/4)):
        numOfRounds = numOfRounds + 1
    return numOfRounds

def tourneyTime(numOfRounds, setTime):
    totTime = numOfRounds * setTime
    hours = math.floor(totTime/60)
    mins = (totTime % 60)
    print("Tournament Time: " + str(hours) + " hours and " + str(mins) + " minutes!\n")

print("TO Tools v1.0")
numPeople = input("How many people in the tournament? ")
setTime = input("How long, on average, do you expect a set to take (in minutes)? ")
a = int(numPeople)
setTime = int(setTime)
numOfRounds = numOfDERounds(a)
tourneyTime(numOfRounds, setTime)
print("Note: This estimate is somewhat pessimistic. It assumes that Grand Finals has 2 sets\nand follows the path through bracket that plays the most sets. Considering this, \nthe estimate is likely over the actual tournament runtime.")
