
def coinToss(tosses):
	print "Starting the program..."
	headCount = 0
	tailCount = 0
	for x in range(1, tosses + 1):
		import random
		num = round(random.random(),0) / 100 * 99
		y = '{0:g}'.format(float(x))
		if num == 0.0:
			headTail = "head"
			headCount += 1
		else:
			headTail = "tail"
			tailCount += 1
		print "Attempt #" + y + ": Throwing a coin... It's a " + headTail + "! ... Got", headCount, "head(s) so far and", tailCount, "tail(s) so far" 
	print "Ending the program, thank you!"

coinToss(5000)