def add(x,y):
	z = x + y
	print("{} + {} = {}".format(x, y, z))
	return z
	
def subtract(x,y):
	z = x - y
	print("{} - {} = {}".format(x, y, z))
	return z
	
def multiply(x,y):
	z = x * y
	print("{} x {} = {}".format(x, y, z))
	return z
	
x = input("enter a letter :")
print("you entered {}".format(x))

if x == "a":
	d = add(13,21)
elif x == "s":
	e = subtract(20, 16)
elif x == "m":
	f = multiply(2, 5)

print("done")