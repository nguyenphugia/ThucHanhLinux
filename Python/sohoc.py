a = int(input("A = "))
b = int(input("B = "))
def cong(a,b):
	tong= a + b
	print "Tong = " ,tong
cong(a,b)
def tru(a,b):
	hieu= a - b
	print "Hieu = " ,hieu
tru(a,b)
def nhan(a,b):
	tich= a * b
	print "Tich = " ,tich
nhan(a,b)
def chia(a,b):
	thuong= a / b
	print "Thuong =" ,thuong
chia(a,b)
def chiald(a,b):
	thuong= a/b
	sodu=a-(thuong * b)
	print "Ket qua = ",thuong," du ",sodu
chiald(a,b)
def luythua(a,b):
	luythua = 1
	i = 1
	while i<=b:
		luythua=luythua*a
		i = i+1
	print "Luythua = ",luythua
luythua(a,b)


