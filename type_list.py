#concatenates strings and adds integers in list and gives
#analysis of list contents
def typeList(list1):
	elementString = ""
	elementNum = 0
	
	for element in list1:
		if type(element) == str:
			elementString += element + " "
		elif type(element) == int or float:
			elementNum += element

	if elementString != "" and elementNum == 0:
		print "The list you entered is of string type"
		print "String: ", elementString

	elif elementString == "" and elementNum != 0:
		print "The list you entered is of integer type"	
		print "Sum: ", elementNum

	else:
		print "The list you entered is of mixed type"
		print "String: ", elementString 	
		print "Sum: ", elementNum

list1 = ['magical unicorns',19,'hello',98.98,'world']
typeList(list1)	

list1 = [2,3,1,7,4,12]
typeList(list1)	

list1 = ['magical','unicorns']
typeList(list1)	