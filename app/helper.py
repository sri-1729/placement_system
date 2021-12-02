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
	string = str(string)
	x = string.split(" ")
	only_date = x[0]
	y = only_date.split('-')
	y.reverse()
	final = '-'.join(y)
	return str(final)

def formatString(string):
	final = ''
	for each in string:
		if each == ',':
			break
		if each != '(':
			final = final + each
	return str(final)

def extract_date_httpFormat(string):
	string = str(string)
	#'2021-14-09 00:00:00'
	x = string.split(" ")
	only_date = x[0]
	y = only_date.split('-')
	final = '-'.join(y)
	return str(final)

