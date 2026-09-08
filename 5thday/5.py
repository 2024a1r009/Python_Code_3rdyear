p=input("Enter: ")
length=len(p)
flag=0
for i in p:
    if i=="@":
        flag=1

t=p[0]
t1=p[-1]
if flag==1:
    print("@ is present")
else:
    print("@ is absent")  
if t==t1:
    print("Yes,They are sme")
else:
    print("They are different") 
