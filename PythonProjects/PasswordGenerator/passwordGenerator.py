import random
def generate_password(dlugosc_hasla, znaki_specjalne):
    if (znaki_specjalne == "tak" or znaki_specjalne == "Tak"):
        while(dlugosc_hasla >= 0):
            rn = random.randint(0,9)
            rs = random.randint(0,23)
            rb = random.randint(0,23)
            rc = random.randint(0,6)
            r = random.randint(0,12)
            if(r == 0 or r == 4 or r == 8 or r == 12):
                password.append(numbers[rn])
            if(r == 1 or r == 5 or r == 9):
                password.append(smallLetters[rs])
            elif(r == 2 or r == 6 or r == 10):
                password.append(bigLetters[rb])
            elif(r == 3 or r == 7 or r == 11):
                password.append(characters[rc])
            dlugosc_hasla-=1
    else:
        while(dlugosc_hasla >= 0):
            rn = random.randint(0,9)
            rs = random.randint(0,23)
            rb = random.randint(0,23)
            rc = random.randint(0,6)
            r = random.randint(0,12)
            if(r == 0 or r == 4 or r == 8 or r == 12):
                password.append(numbers[rn])
            if(r == 1 or r == 5 or r == 9):
                password.append(smallLetters[rs])
            elif(r == 2 or r == 6 or r == 10):
                password.append(bigLetters[rb])
            
            dlugosc_hasla-=1



numbers = ['0','1','2','3','4','5','6','7','8','9']
smallLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','p','o','q','r','s','t','u','w','y','z']
bigLetters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','Y','Z']
characters = ['!','@','#','$','%','&','*']
password = []
i = int(input("Jak dlugie ma byc haslo? "))


choice = input('Czy haslo ma miec znaki specjalne? Jesli tak to napisz "tak". Jesli haslo nie ma zawierac znakow specjalnych kliknij enter: ')

generate_password(i,choice)
def convert_list_to_string(org_list, separator = ''):
    return separator.join(org_list)

full_password = convert_list_to_string(password, '')

whatfor = input("Do czego jest to haslo? ")
f = open("passwords.txt", "a")
f.write(whatfor+": "+full_password+"\n")
f.close()
print("Twoje haslo: "+full_password)
