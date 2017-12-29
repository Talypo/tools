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
    if (a <= 1):
        return 0
    elif(a == 2):
        return 2
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

def numOfRRRounds(a):
    if (a % 2 == 0):
        return a
    else:
        return (a+1)

def tourneyTime(numOfRounds, setTime):
    totTime = numOfRounds * setTime
    hours = math.floor(totTime/60)
    mins = (totTime % 60)
    print("Running Time: " + str(hours) + " hour(s) and " + str(mins) + " minutes!\n")
    return totTime

def tourneyRuntime():
    Ttype = input("Is this a Double-Elimination or Round-Robin tournament (DE/RR)? ")
    while ((Ttype != "DE") & (Ttype != "RR")):
        Ttype = input("Please type DE or RR:")
    numPeople = input("How many people in the tournament? ")
    numPeople = int(numPeople)
    if (Ttype == "RR"):
        numPools = input("How many pools will the RR stage have (If tournament is RR only, say 1)? ")
        numPools = int(numPools)
        pplPerPool = int(math.ceil(numPeople / numPools))
        pplAdvancing = input("How many people advance to bracket from each pool (If tournament is RR only, say 1)? ")
        pplAdvancing = int(pplAdvancing)
        numDEPeople = pplAdvancing * numPools
    setTime = input("How long, on average, do you expect a set to take (in minutes)? ")
    setTime = int(setTime)
    if (Ttype == "DE"):
        numOfDRounds = numOfDERounds(numPeople)
        print("\n")
        tourneyTime(numOfDRounds, setTime)
    else:
        numOfRRounds = numOfRRRounds(pplPerPool)
        numOfDRounds = numOfDERounds(numDEPeople)
        print("\nRound Robin stage:")
        RRTime = tourneyTime(numOfRRounds, setTime)
        print("\nDouble Elimination stage:")
        DETime = tourneyTime(numOfDRounds, setTime)
        totTime = RRTime + DETime
        hours = math.floor(totTime/60)
        mins = (totTime % 60)
        print("\nTotal Tournament Time: " + str(hours) + " hour(s) and " + str(mins) + " minutes!\n")
    print("\n\nNote: This estimate is somewhat pessimistic. It assumes that Grand Finals has 2 sets\nand follows the path through bracket that plays the most sets (for DE). Considering this, \nthe estimate is likely over the actual tournament runtime for double-elimination.")

print("TO Tools v1.1")
tourneyRuntime()
