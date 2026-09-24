# WAP a python  prog to input a number and reverse it using arithemtic operation
n=int(input("Enter : "))
s=""
while n!=0:
    t=n%10
    s+=str(t)
    n=n//10

print(s)    



