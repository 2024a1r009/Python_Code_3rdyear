# wap to input nos in a list and create two sep list for even and odd no 
l1=list(map(int,input().strip().split()))
l2=[]
l3=[]
for i in l1:
    if i%2==0:
        l2.append(i)
    else:
        l3.append(i)

print("Even :", l2)
print("Odd :", l3)

