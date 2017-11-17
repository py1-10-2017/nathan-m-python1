class MathDojo(object):
	def __init__(self):
		self.total = 0

	def add(self, *nums):
		add_total = 0
		for i in range(len(nums)):
			if type(nums[i]) == list or type(nums[i]) == tuple:
				mini_sum = sum(nums[i])
				add_total += mini_sum

			else: 	
				add_total += nums[i]

		self.total += add_total
		return self	


	def subtract(self, *nums):
		subtract_total = 0
		for i in range(len(nums)):
			if type(nums[i]) == list or type(nums[i]) == tuple:
				mini_sum = sum(nums[i])
				subtract_total -= mini_sum

			else:				
				subtract_total -= (nums[i])
			
		self.total += subtract_total
		return self	
		

	def result(self):
		print self.total

# md = MathDojo()
# md.add(2).add(2,5).subtract(3,2).result()

md = MathDojo()
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()