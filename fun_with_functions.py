

#Odd/Even- Shows even and odd number from 1 to 2000
for num1 in range (1, 2001):
	if num1 % 2 == 0:
		print "Number is", num1,". This is an even number."
	if num1 % 2 != 0:
		print "Number is", num1,". This is an odd number."

#Muliply- Iterates through each value in a list (e.g. a = [2, 4, 10, 16]) 
#and returns a list where each value has been multiplied by 5.

def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b


#Takes the multiply function call as an argument and
#returns the multiplied list as a two-dimensional list. 

def layered_multiples(arr):
	new_array = []
	for z in range(len(arr)):
		a = arr[z]
		b = []
		for x in range(1, a + 1):
			b.append(1)
		new_array.append(b)
 	return new_array
x = layered_multiples(multiply([2,4,5],3))
print x
#output
#>>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]