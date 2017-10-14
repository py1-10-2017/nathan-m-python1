weekend = {"Sun": "Sunday", "Sat": "Saturday"} #literal notation
capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"

#prints dictionary values
def checkDic1(dic):
	for val in dic.itervalues():
		print val

checkDic1(weekend)	

#prints dictionary keys and values
def checkDic2(dic):
	for key,data in dic.iteritems():
		print key, "=", data

checkDic2(capitals)	