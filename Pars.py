import re
too_big = 20
pattern4 = re.compile("[\.\\;:\^\{\}\|\_\-\!@$\%&*\(\)]+")
pattern1 = re.compile("\w([\.\\;:\^\{\}\|\_\-\!@$%&*\(\)]+)\w")
pattern2 = re.compile("(\w|^)([0-9]+)(\w+)")
pattern3 = re.compile("([0-9]+)(\w+)")

def Pars(token):
	exit = 1
	counter1 = 0
	counter2 = 0
	low_letter = 0

	for word in token:
		if word == "":
			exit =  0
		elif re.search(pattern2, word) or re.search(pattern3, word):
			counter2 += 1
			print(word)
			exit =  0
		elif re.search(pattern1, word) or re.search(pattern4, word):
			counter1 += 1
			print(word)
			exit = 0
		elif len(word) > too_big:
			low_letter += 1
			print(word)
			exit = 0
		if exit == 0:
			break
	return exit
	# return [counter1, counter2, low_letter]

# print(Pars(["%%$%$^%%E%%%", "77gyy", "vrcuetvveitbveyvetbe" ]))