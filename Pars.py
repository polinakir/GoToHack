import re
critical_count_letter = 20
pattern1 = re.compile("\b([\.\\;:\^{}|]+)\b")
pattern2 = re.compile("\w[0-9]+\w")
pattern3 = re.compile("^http://(\w+)")

def Pars(text):
	counter1 = 0
	counter2 = 0
	low_letter = 0
	if isinstance(text, str):
		pairs_text = text.split()
	else:
		pairs_text = text
	
	for word in pairs_text:
		if re.search(pattern3, word):
			pass
		elif re.search(pattern2, word):
			counter2 += 1
			return 0
			print(word)
		elif re.search(pattern1, word):
			counter1 += 1
			return 0
			print(word)
		elif len(word) > critical_count_letter:
			low_letter += 1
			return 0
			print(word)
	return 1
	# return [counter1, counter2, low_letter]