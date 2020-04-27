def ou(x,y):
	if y>x:
		x,y=y,x
	z=x%y
	if z==0:
		return y
	return ou(y,z)