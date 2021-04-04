import sys
keyword = ""

keyword = sys.argv[1:]
if(keyword == ""): quit()
keyword = str("".join(keyword)).lower()
print("")
keyword = sorted(keyword+"a")
keyword = list(dict.fromkeys(keyword))
for letter in keyword:
	letter =  ord(letter)
	if(96>letter>122): 
		continue
	for _ in range(26):
		if(letter <= 122):
			print(chr(letter), end=" ")
			letter+=1
		else:
			print(chr(letter-26), end=" ")
			letter+=1	
	print("")