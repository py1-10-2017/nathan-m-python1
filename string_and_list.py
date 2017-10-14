words = "It's Thanksgiving day. It's my birthday,too!"
print "Find: ", words.find('day')

monthDay = words.replace('day', 'month')
print "Replace: ", monthDay

x = [2,54,-2,7,12,98]
print "Min: ", min(x);
print "Max: ", max(x);

y = ["hello",2,54,-2,7,12,98,"world"]
print "First: ", y[0]
print "Last: ", y[(len(y)-1)]
a = [y[0], y[(len(y)-1)]]
print "First & Last List: ", a

z = [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort(); 
b = z[:(len(z)/2)]
c = z[(len(z)/2):]
c[0] = b
print "New List: ", c

