#4.1
from Sinhvien import *
from khoa import *
#nhapdssv
print "--------danh sach sinh vien-------"
listsv=[]
sv=Sinhvien("001","Mai A","57")
listsv.append(sv)
sv=Sinhvien("002","Tran B","58")
listsv.append(sv)
sv=Sinhvien("003","Le C","57")
listsv.append(sv)
sv=Sinhvien("004","Pham Q","58")
listsv.append(sv)
sv=Sinhvien("005","Ngo M","59")
listsv.append(sv)
#in dssv
size = len(listsv)
i=0
while i<size:
	listsv[i].toString()
	i=i+1
#nhap dsk
print "---------danh sach khoa--------"
listkhoa=[]
kh=Khoa("56","K 56CNTT")
listkhoa.append(kh)
kh=Khoa("57","K 57CNTT")
listkhoa.append(kh)
kh=Khoa("58","K 58CNTT")
listkhoa.append(kh)
kh=Khoa("59","K 59CNTT")
listkhoa.append(kh)
#in dsk
size = len(listkhoa)
n=0
while n<size:
	listkhoa[n].toString()
	n=n+1
#4.2
size = len(listsv)
m=0
print "----danh sach sinh vien K57----"
while m<size:
	if listsv[m].getKhoa()=="57":
		listsv[m].toString()
	m = m+1
