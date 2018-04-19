n = int(input("N = "))
def Tinh(n):
	i=1
	tong=0
	print "day so: "
	while i<=n:
		print i
		if(i%2==0):
			tong=tong+i
		i=i+1
	print "Tong cac phan tu chan: ",tong
Tinh(n)

	
