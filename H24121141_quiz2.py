m=eval(input('Enter the shopping amount:'))  #輸入購物金額
l=input('Enter the membership level(Regular or Gold):')  #輸入會員等級
if l=='Regular':  #判定是Regular，以下是隨著購物金額改變，所折扣的%也不同
	if m<1000:
		print(l,m)
	elif m<2000 and m>1000:
		print(l,m*0.9)
	elif m>2000 and m<3000:
		print(l,m*0.85)
	elif m>3000:
		print(l,m*0.8)
if l=='Gold':  #判定是Gold，以下是隨著購物金額改變，所折扣的%也不同
	if m<1000:
		print(l,m)
	elif m<2000 and m>1000:
		print(l,m*0.85)
	elif m>2000 and m<3000:
		print(l,m*0.8)
	elif m>3000:
		print(l,m*0.75)
if l!='Regular' and l!='Gold':  #如果兩者(Regular or Gold)皆不是，則顯示以下字串
	print('Invalid member level. Please enter "Regular" or "Gold"')