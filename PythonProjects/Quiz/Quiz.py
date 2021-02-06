import time


answer = []
question = []
userAnswer = ""
questionNumber = 0
points = 0


def Ask():
    global questionNumber, points
    userAnswer = input("What is your answer?")
    if(userAnswer.upper() == answer[questionNumber]):
        points += 1
        print("Good answer, now wait for next question")
        time.sleep(1)
    else:
        print("Wrong answer, now wait for next question")
        time.sleep(1)


def readFromFile():
    global questionNumber
    try:
        f = open("questions.txt", "r")
    except:
        print("Couldn't open a file!")
        quit()
    lines = f.readlines()
    numberOfLines = len(lines)
    i = 1
    while i < numberOfLines:
        if i % 6 == 0:
            answer.append(lines[i].strip())
            Ask()
            questionNumber += 1
            i += 1
            continue
        print(lines[i])
        i += 1
    percent = ((points/questionNumber)*100)
    percent = round(percent)
    print("Good job you finished this quiz, your score is: %d/%d it is %d%% " %
          (points, questionNumber, percent))
    f.close()
