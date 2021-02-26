import convert as c

def do():
    print("Would you like to encode or decode Morse Code? ")
    choice = input("Chose 1 to encode \nChose 2 to decode\n")
    if (choice == "1"):
        code = input("Type a world that you want to encode: ")
        c.textToMorse(code)
    elif choice == "2":
        code = input("\nType a world that you want to decode: ")
        c.morseToText(code)
    else:
        print("Some thing gone wrong try again")
        do()

print("Welcome to my Morse code encoder/decoder")
while True:
    do()
    end = input("\nWould you like to encode/decode again? (yes/no) ")
    if( end.lower() == "yes"):
        continue
    else:
        break



