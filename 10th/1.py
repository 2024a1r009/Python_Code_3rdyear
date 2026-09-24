# wap to input marks of n stds in a list. Display highest marks, lowest marks,avg marks and no of dtudents who passed
n=list(map(int,input().strip().split()))
max=n[0]
for i in n:
    if i>max:
        max=i

print(max)
min=0
for i in n:
    if i<min:
        min=i

print(min)  
sum=0
for i in n:
    sum+=i

avg=sum//2
print(avg)

