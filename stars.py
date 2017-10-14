
#takes a list of numbers and multiplies it by "*"
x = [4, 6, 1, 3, 5, 7, 25]
def draw_stars(arr1):
	for z in range(0, len(x)):
		print "*" * arr1[z]

draw_stars(x)

#shows ints in list * "*" and first 
#letter of string * length of string
y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def draw_stars(arr1):
	for z in range(0, len(arr1)):
		b = arr1[z]
		if type(b) is int:
			print "*" * b 
		else:
			print b[0].lower() * len(b)	
		

draw_stars(y)

