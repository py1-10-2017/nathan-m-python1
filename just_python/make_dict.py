#takes in two lists and creates a single dictionary 
#if of even length, items the first list will be returned as the "keys"
#If the lists are of unequal length, the longer list will be 
#returned as the keys and the items in the shorter list will be returend 
#as the values.

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "bears"]

def make_dict(arr1, arr2):
  	if len(arr1) > len(arr2):
  		new_dict = dict(zip(arr2, arr1))
	else:	
  		new_dict = dict(zip(arr1, arr2))
  	return new_dict


print make_dict(name, favorite_animal)