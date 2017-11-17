class Call(object):
	def __init__(self, id, name, phone, time, reason):
		self.id = id
		self.name = name
		self.number = phone
		self.time = time
		self.reason = reason

	def display_all(self):
		print "ID: ", str(self.id)
		print "Name: ", self.name
		print "Number: ", str(self.number)
		print "Time:", str(self.time)
		print "Reason: ", self.reason
			

class CallCenter(object):
	def __init__(self):
		self.calls = []
		self.queue_size = len(self.calls)

	def add(self, call):
		self.calls.append(call)
		self.queue_size += 1
		return self

	def remove(self):
		self.calls.pop(0)
		self.queue_size -= 1
		return self

	def info(self):
		for call in self.calls:
			print call.name, call.number
		print "queue =", self.queue_size


callcenter = CallCenter()
call1 = Call(1, "Dick", "555-1212", "10:00", "evil spirits")
call2 = Call(2, "Dale", "555-1212", "11:00", "alien abduction")
call3 = Call(3, "Dave", "555-1212", "11:30", "sasquatch")

callcenter.add(call1).add(call2).add(call3).remove().info()

