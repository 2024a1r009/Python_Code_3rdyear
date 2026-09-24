# wap to input marks of 10 std. Store only valid n=marks btw 0 and 100 in a list.
n=list(map(int,input().strip().split()))
l2=[]
for i in n:
    if i>=0 and i<=100:
        l2.append(i)

print(l2)        
