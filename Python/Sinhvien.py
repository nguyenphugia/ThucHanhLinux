class Sinhvien:
	def __init__(self,mssv,hoten,khoa):
		self.mssv=mssv
		self.hoten=hoten
		self.khoa=khoa
	def setMSSV(self,mssv):
		self.mssv=mssv
	def setTen(self,ten):
		self.ten=ten
	def setKhoa(self,khoa):
		self.khoa=khoa
	def getMSSV(self):
		return self.mssv
	def getTen(self):
		return self.ten
	def getKhoa(self):
		return self.khoa
	def toString(self):
		print self.mssv," - ",self.hoten," - ",self.khoa
