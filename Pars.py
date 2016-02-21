import re
critical_count_letter = 20
pattern1 = re.compile("\b[\.\\;:\^{}|]+\b")
pattern2 = re.compile("\b[0-9]+\b")
def Pars(text):
	if isinstance(text, str):
		pairs_text = text.split()
	else:
		pairs_text = text
	
	for word in pairs_text:
		if re.search(pattern1, word):
			print(word)
		elif re.search(pattern2, word):
			# critical
			print(word)
		elif len(word) > critical_count_letter:
			print(word)