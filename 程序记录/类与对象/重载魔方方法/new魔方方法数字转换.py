class C2F(float):
	def __new__(cls,x):
		x=float(x)*1.8+32
		return float.__new__(cls,x)