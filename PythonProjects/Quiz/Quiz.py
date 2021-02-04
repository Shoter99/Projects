answer = []
def readFromFile():
    try:
        f = open("questions.txt", "r")
    except:
        print("Couldn't open a file!")
        quit()
    lines=f.readlines()
    numberOfLines = len(lines) 
    i = 1
    while i < numberOfLines:
        if i%6 == 0:
            answer.append(lines[i].strip())
            i+=1
            continue
        print(lines[i])
        i+=1

    f.close()
