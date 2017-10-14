for num1 in range(1, 1000): #prints all odd numbers
	if num1 % 2 != 0:		#from 1-1000
		print num1

for num2 in range(5, 1000000): #prints all multiples of 5
	if num2 % 5 == 0:		   #from 5 to 1,000,000
		print num2

a = [1, 2, 5, 10, 255, 3] #prints sum of numbers in list a
x = 0
y = 0
while x < len(a): 
	y = y + a[x]
	x += 1
print y

a = [1, 2, 5, 10, 255, 3] #prints average of numbers in list a
x = 0
y = 0
while x < len(a): 
	y = y + a[x]
	x += 1
print y / len(a)