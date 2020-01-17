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
	
def divide(x,y):
	z = x/y
	print("{} / {} = {}".format(x, y, z))
	return z
	
x = input("enter a letter :")
print("you entered {}".format(x))
num1 = float(input("input the first number: "))
num2 = float(input("input a second number: "))

if x == "a":
	d = add(num1,num2)
elif x == "s":
	e = subtract(num1, num2)
elif x == "m":
	f = multiply(num1, num2)
elif x == "d":
	g = divide(num1, num2)

print("done")