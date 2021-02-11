def hanoi(sizeOfTower, startingPlace, finishingPlace):
    global sizeOfTower
    if sizeOfTower == 1:
        print("Move form %d to %d" % (startingPlace, finishingPlace))
        return 1
    temporaryPlace = 6 - startingPlace - finishingPlace
    hanoi(sizeofTower-1, startingPlace, temporaryPlace)
    print("Move from %d to %d" % (temporaryPlace, startingPlace))
    hanoi(sizeofTower-1, startingPlace, finishingPlace)


sizeOfTower = int(input("Type size of hanoi tower"))
startingPlace = int(input("Type starting place"))
finishingPlace = int(input("Type finishing place"))
hanoi(sizeOfTower, startingPlace, finishingPlace)
