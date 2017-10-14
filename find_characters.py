#takes a list of strings and a string containing a single character, 
#and prints a new list of all the strings containing that character.

checkWord = ""
new_list = []
word_list = ['hello','world','my','name','is','Anna'];
char = 'o'

for checkWord in word_list:
	if checkWord.find(char) != -1:
		new_list.append(checkWord);		
print new_list
