def createChars():
    asciiChar = []
    x = 0
    while x+65 <= 90:
        asciiChar.append(chr(x+65))
        x+=1
    x=0
    while x+48 < 58:
        asciiChar.append(chr(x+48))
        x+=1
    return asciiChar
def createMorse():
    morseCode = {
        'A': "._",
        'B': "_...",
        'C': "_._.",
        'D': "_..",
        'E': ".",
        'F': ".._.",
        'G': "__.",
        'H': "....",
        'I': "..",
        'J': ".___",
        'K': "_._",
        'L': "._..",
        'M': "__",
        'N': "_.",
        'O': "___",
        'P': ".__.",
        'Q': "__._",
        'R': "._.",
        'S': "...",
        'T': "_",
        'U': ".._",
        'V': "..._",
        'W': ".__",
        'X': "_.._",
        'Y': "_.__",
        'Z': "__..",
        '1': ".____",
        '2': "..___",
        '3': "...__",
        '4': "...._",
        '5': ".....",
        '6': "_....",
        '7': "__...",
        '8': "___..",
        '9': "____.",
        '0': "_____"
    }
    return morseCode
def textToMorse(input):
    morse = createMorse()
    for x in input.upper():
        if(x == " "):
            print(" ",end="")
        elif(morse.get(x)):
            print(morse.get(x)+" ", end="")
        else: 
            print("Your input is not a word or it has special characters which are not accepted by this encoder")
            break
def morseToText(input):
    input = input+" "
    morse = createMorse()
    output = ""
    for x in input:
        if(x == " "):
            if output in morse.values():
                print(list(morse.keys())[list(morse.values()).index(output)],end="") 
                output = ""
            else:
                print("Your input hava characters not accepted by this decoder you are allowed to only use '.' and '_'")
                break
        else:
            output+=x

