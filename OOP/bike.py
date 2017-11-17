class Bike(object):
	def __init__(self, price, max_speed, miles):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0

	def displayinfo(self):
		print self.price, self.max_speed, self.miles
	
	def ride(self):
		print "Riding"
		self.miles += 10
		return self

	def reverse(self):
		print "Reverse"
		self.miles -= 5
		if self.miles < 0:
			self.miles = 0
		return self


bike1 = Bike(500, "28mph", 1200)
bike1.ride().ride().ride().reverse().displayinfo()

bike2 = Bike(200, "16mph", 4200)
bike2.ride().ride().reverse().reverse().displayinfo()

bike3 = Bike(800, "31mph", 150)
bike3.reverse().reverse().reverse().displayinfo()