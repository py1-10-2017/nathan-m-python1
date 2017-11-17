class Patient(object):
	num_patients = 0
	def __init__(self, name, allergies):
		self.name = name
		self.allergies = allergies		
		Patient.num_patients += 1	
		self.id = Patient.num_patients
		self.bed_num = None

	


class Hospital(object):
	def __init__(self, hospital_name, capacity):
		self.hospital_name = hospital_name
		self.capacity = capacity
		self.patients = []
		self.beds = ["open"] * self.capacity

	def admit(self, patient):
		if len(self.patients) < self.capacity:
			self.patients.append(patient)
			for i in range(0, len(self.beds)):
				if self.beds[i] == "open":
					patient.bed_num = i + 1
					self.beds[i] = "full"
					print "Patient {} admitted to bed {}".format(patient.id, patient.bed_num)
					break
		else:
			print "The Hospital is full"
		return self	

	def discharge(self, patient_id):
		for patient in self.patients:
			if patient.id == patient_id:
				self.beds[patient.bed_num - 1] = "open"
				self.patients.remove(patient)			
				print "Patient {} discharged from bed {}".format(patient_id, patient.bed_num)
		return self

patient1 = Patient("Dick", "peanuts")
patient2 = Patient("Dale", "apples")
patient3 = Patient("Don", "mangos")
patient4 = Patient("Dave", "peaches")
patient5 = Patient("Dom", "cashews")
patient6 = Patient("Dan", "walnuts")
patient7 = Patient("Duke", "pears")
patient8 = Patient("Dax", "pecans")
patient9 = Patient("Doug", "bananas")

hospital1 = Hospital("Kaiser", 8)
hospital1.admit(patient1).admit(patient2).admit(patient3).admit(patient4).admit(patient5).admit(patient6).admit(patient7).admit(patient8).admit(patient9).discharge(3).admit(patient9)

