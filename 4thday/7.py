p=input("Enter email: ")
flag=0
for i in p:
    if i=='@':
        flag=1
c=0        
for i in p:
    c+=1

# print(c)  
if c>=8 and flag ==1:
    print("True")
else:
    print("False")    


        