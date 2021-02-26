def createChars():
    asciiChar = []
    x = 0
    while x+65 <= 90:
        asciiChar.append(chr(x+65))
        x += 1
    x = 0
    while x+48 < 58:
        asciiChar.append(chr(x+48))
        x += 1
    return asciiChar


def createMorse():
    morseCode = {
        'A': ".-",
        'B': "-...",
        'C': "-.-.",
        'D': "-..",
        'E': ".",
        'F': "..-.",
        'G': "--.",
        'H': "....",
        'I': "..",
        'J': ".---",
        'K': "-.-",
        'L': ".-..",
        'M': "--",
        'N': "-.",
        'O': "---",
        'P': ".--.",
        'Q': "--.-",
        'R': ".-.",
        'S': "...",
        'T': "-",
        'U': "..-",
        'V': "...-",
        'W': ".--",
        'X': "-..-",
        'Y': "-.--",
        'Z': "--..",
        '1': ".----",
        '2': "..---",
        '3': "...--",
        '4': "....-",
        '5': ".....",
        '6': "-....",
        '7': "--...",
        '8': "---..",
        '9': "----.",
        '0': "-----"
    }
    return morseCode


def textToMorse(input):
    morse = createMorse()
    for x in input.upper():
        if(x == " "):
            print("/", end="")
        elif(morse.get(x)):
            print(morse.get(x)+" ", end="")
        else:
            print(
                "Your input is not a word or it has special characters which are not accepted by this encoder")
            break


def morseToText(input):
    input = input+" "
    morse = createMorse()
    output = ""
    for x in input:
        if(x == " " or x == "\n"):
            if output in morse.values():
                print(list(morse.keys())[
                    list(morse.values()).index(output)].lower(), end="")
                output = ""
            else:
                print(
                    "Your input hava characters not accepted by this decoder you are allowed to only use '.' and '_'")
                break
        elif x == "/":
            print(" ", end="")
        else:
            output += x
