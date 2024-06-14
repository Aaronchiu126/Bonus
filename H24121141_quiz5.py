size=eval(input('Enter the size of the grid:'))
k=0
for i in range(size):
	for j in range(size):
		print('_',end=' ')
		if j==size-1:
			print()
while k>=0:   #開始改變圖形的元素
	cellc=input('Enter the cell coordinates to edit:').split(',')
	cell=input('Enter the new value for the cell:')
	column=int(cellc[0])
	row=int(cellc[1])
	for x in range(size):
		for y in range(size):
			if (x,y)==(column,row):  #更換圖形條件
				print(cell,end=' ')
				if y==size-1:
					print()
			else:
				print('_',end=' ')
				if y==size-1:
					print()
	if cellc=="done":
		break
	


