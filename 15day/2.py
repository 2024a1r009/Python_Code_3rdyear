# WAP to perform searching activity using linear and binary search..
n=int(input("Enter the elmt: "))
l=list(map(int,input().strip().split()))
t=int(input("Enter the target: "))
pos=-1
for i in range(len(l)):
    if l[i]==t:
        pos=i
        break
if pos!=-1:
    print(pos)
else:
    print("Not found")    
sort_n=sorted(l)
print(sort_n)

low=0
high=len(sort_n)-1
bpos=-1
while low<=high:
    mid=(low+high)//2
    if sort_n[mid]==t:
        bpos=mid
        break
    elif sort_n[mid]<t:
        low=mid+1
    else:
        high=mid-1

if bpos!= -1:
    print(bpos)
else:
    print("Not found")    
   


    

