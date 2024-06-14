s=input('Enter a sequence of integers separated by whitespace:').split()
slength=len(s)
lics=[]
y=[]
for i in range(0,slength,1): #列表迴圈將值填入列表
	if i < slength-1:
		if int(s[i+1])>=int(s[i]): #如果值比前一個大就會填入
			y.append(int(s[i]))
		else:
			if len(y)>len(lics):
				lics=y
				y=[]
	else:
		if int(s[i])>=int(s[i-1]):
			y.append(int(s[i]))
		else:
			if len(y)>len(lics):
				lics=y
				y=[]
licslength=len(lics)
print('length=',licslength)
print('Lics:',lics)
