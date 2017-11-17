class Product(object):
	def __init__(self, price, item_name, weight, brand):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.status = "for sale"

	def sell(self):
		self.status = "sold"
		return self

	def add_tax(self, tax):
		self.price += (self.price * tax)
		return self

	def returns(self, condition):
		if condition =="defective":
			self.status = "defective"
			self.price = 0
		if condition == "returned_in_box_like_new":
			self.status = "for sale"
		if condition == "opened":
			self.status = "used"
			discount = .20
			self.price -= self.price * discount
		return self	

	def display_info(self):
		print "Price: ", self.price
		print "Item Name: ", self.item_name
		print "Weight: ", self.weight
		print "Brand: ", self.brand
		print "Status: ", self.status		

toy = Product(20, 'Transformer', '3 lbs.', 'Hasbro')
toy.sell().add_tax(.06).returns('returned_in_box_like_new').display_info()
