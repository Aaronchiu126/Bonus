print('Welcome to the simple calculator program!')
i=0
while i==0:   #進入計算機的迴圈
	f=int(input('Enter the first number:'))
	s=int(input('Enter the second number:'))
	o=input('Select an arithmetic operation (+,-,*,/):')
	if o=='+':
		print('Result:',f+s)
		q=input('Do you want to perform another calculation?(yes or no):')
		if q=='yes':
			i=0
		else:
			i=1
			print('Goodbye!')
	if o=='-':
		print('Result:',f-s)
		q=input('Do you want to perform another calculation?(yes or no):')
		if q=='yes':
			i=0
		else:
			i=1
			print('Goodbye!')
	if o=='*':
		print('Result:',f*s)
		q=input('Do you want to perform another calculation?(yes or no):')
		if q=='yes':
			i=0
		else:
			i=1
			print('Goodbye!')
	if o=='/':
		if s==0:
			print('division by zero')
			q=input('Do you want to perform another calculation?(yes or no):')
		else:
			print('Result:',f/s)
			i=0
			q=input('Do you want to perform another calculation?(yes or no):')
		if q=='yes':
			i=0
		else:
			i=1
			print('Goodbye!')
