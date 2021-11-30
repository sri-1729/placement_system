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

def extract_date(string):
	#'2021-14-09 00:00:00'
	x = string.split(" ")
	print(x)
	only_date = x[0]
	y = only_date.split('-')
	y.reverse()
	final = '-'.join(y)
	return str(final)

