a = int(input("A = "))
b = int(input("B = "))
def swap(a,b):
	tam =a
	a=b
	b=tam
	print "sau khi doi: \nA = ",a, "\nB = ",b
print "truoc khi doi: "
print "A = ",a,"\nB = ",b
swap(a,b)
