#Generates ten scores between 60 and 100. Each time a score is 
#generated, the grade for the particular score is displayed.
def grades(score):		
	random_float = round((score*40 + 60),0)
	random_int = '{0:g}'.format(float(random_float))
	#print random_int
	if random_float < 70:
		print "Score: " + random_int + "; Your grade is D"
	elif 70 <= random_float < 80:
		print "Score: " + random_int + "; Your grade is C"
	elif 80 <= random_float < 90:
		print "Score: " + random_int + "; Your grade is B"
	else:
		print "Score: " + random_int + "; Your grade is A"
			
import random
for x in range(0, 10):
	grades(random.random())
