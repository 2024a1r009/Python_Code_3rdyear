# wap to rotate a list one pos to the right
lt=list(map(int,input().strip().split()))
print(lt)
l2=[]
for i in range(len(lt)-1):
    l2.append(lt[i+1])

l2.append(lt[0])

print(l2)    
    