def isnum(char):
	if char >= '0' and char <='9':
		return True
	return False


def strToInt(string):
	#(345,)
	final = ''
	for each in string:
		if(isnum(each)):
			final = final + each
	return int(final)