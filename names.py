#outputs first and last names
students = [
     {'first_name' : 'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

for x in range(0, len(students)):
	allItems = str(students[x])
	firstName = allItems[allItems.find(":") + 3 : allItems.find(",") - 1]
	lastName = allItems[allItems.find(":", allItems.find(":") + 1) + 3 : allItems.find("}") - 1]
	print firstName, lastName


#Prints a specific format format including number of characters in each combined name
users = {
 'Students': [
     {'first_name' : 'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }


def checkDic2(dic):
	for key,data in dic.iteritems():
		print key
		x = 0
		for value in data:
			x += 1
			print x, "-", value["first_name"] + " " + value["last_name"], "-", (len(value["first_name"]) + len(value["last_name"]))			
			


checkDic2(users)

