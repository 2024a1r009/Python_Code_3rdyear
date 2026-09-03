# wap to take string and separate characters present at even index positions and odd index positions.
s=input("Enter : ")
even=[]
odd=[]
for i in range(len(s)):
    if i%2==0:
        even.append(s[i])
    else:
        odd.append(s[i])  

for i in even:
    print(i,end="")
for i in odd:
    print(i,end="")

