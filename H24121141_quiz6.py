l={'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
i=0
num=0  #猜測次數
r1=0   #a-d的猜測次數
r2=0   #e-h的猜測次數
r3=0   #i-l的猜測次數
r4=0   #m-p的猜測次數
r5=0   #q-t的猜測次數
r6=0   #u-x的猜測次數
r7=0   #y-z的猜測次數
def random():  #隨機抽選字母




while i==0:
a=input('Guess the lowcase alphabet:')  #輸入猜測的字母
if random()<int(l[str(a)]):   #判斷隨機字母在猜測字母的前面還是後面
	print('The alphabet you are looking for is alphabetlically lower.')
	num=num+1
elif random()>int(l[str(a)]):
	print('The alphabet you are looking for is alphabetlically higher.')
	num=num+1
else:
	print('congratulation! You are guessed the alphabet',random(),'in',num,'tries')
	break

print()
print('Guess Histogram:')  #顯示猜測次數列表
print('a-d':)
print()
