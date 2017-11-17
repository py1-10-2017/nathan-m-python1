class Animal(object):
	def __init__(self, name, health):
		self.name = name
		self.health = health

	def walk(self):
		self.health -= 1
		return self

	def run(self):
		self.health -= 5
		return self

	def displayHealth(self):
		print "Name: ", self.name
		print "Health: ", self.health
				

class Dog(Animal):
	def __init__(self, name, health):
		super(Dog, self).__init__(name, health)
		self.health = 150

	def pet(self):
		self.health +=5
		return self

class Dragon(Animal):
	def __init__(self, name, health):
		super(Dragon, self).__init__(name, health)
		self.health = 170

	def fly(self):
		self.health += 10
		return self

	def displayHealth(self):
		print "I am Dragon"	
		super(Dragon, self).displayHealth()


animal1 = Animal("Stinky", 50)
animal1.walk().walk().walk().run().run().displayHealth()	

dog1 = Dog("Beagle", 100)
dog1.walk().walk().walk().run().pet().displayHealth()		

dragon1 = Dragon("blister", 100)
dragon1.walk().walk().walk().run().run().fly().displayHealth()			

# mouse1 = Animal("Fievel", 23)
# mouse1.pet().fly().displayHealth()

# dog2 = Dog("Doberman", 200)
# dog2.fly()