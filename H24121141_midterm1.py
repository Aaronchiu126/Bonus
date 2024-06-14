i,j=9,9  #設被乘數與乘數從9開始
while j>0:  #這是乘數的迴圈
	while i>0:  #這是被乘數的迴圈
		print(i,'x',j,'=',i*j,end='\t')
		print(i,'x',j-1,'=',i*(j-1),end='\t')
		print(i,'x',j-2,'=',i*(j-2),end='\n')
		i=i-1
	print()
	j=j-3
	i=9