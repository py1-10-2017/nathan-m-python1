#dictionary about me
nort = {}
nort["name"] = "My name is Nort"
nort["age"] = "My age is 39"
nort["country_of_birth"] = "I was born in the USA"
nort["favorite_language"] = "Python is my favorite language"
nort["mus"] = "I have huge muscles"
nort["nnj"] = "I am trained in ninjitsu"
nort["skt"] = "I have sweet skateboard moves"
nort["looks"] = "I have slicked back hair, glasses and a mustache"
nort["ttop"] = "My cousin's Camaro has t-tops"

#prints dictionary values
def checkDic1(dic):
	for val in dic.itervalues():
		print val

checkDic1(nort)	

#prints dictionary keys and values
def checkDic2(dic):
	for key,data in dic.iteritems():
		print key, "=", data

checkDic2(nort)	