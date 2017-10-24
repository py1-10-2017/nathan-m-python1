
#Takes in a dictionary and returns a list of tuples 
#where the first tuple item is the key and the second is the value. 


my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#prints dictionary keys and values
def checkDic2(dic):
	x = []
	for key,data in dic.iteritems():
		y = (key, data)
		x.append(y)
	return x
print checkDic2(my_dict)	