R=eval(input('please input a Richter scale value:'))  #輸入Richter scale value
E=10**((1.5*R)+4.8)  #算出Equivalence in Joules
TNT=E/(4.184*(10**9))  #算出Equivalence in tons of TNT
N=E/2930200  #算出Equivalence in the number of nutritious lunches
print('Richter scale value:',R)  #顯示Richter scale value
print('Equivalence in Joules:',E)  #顯示Equivalence in Joules
print('Equivalence in tons of TNT:',TNT)  #顯示Equivalence in tons of TNT
print('Equivalence in the number of nutritious lunches:',N)  #顯示Equivalence in the number of nutritious lunches