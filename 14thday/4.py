# WAP to store repeated values in a tuple and count how many times a given value appear 
t=(1,2,"apple", "Banana","apple",1)
n=input("Enter the value : ")
c=0
for i in range(len(t)):
    if str(t[i])==n:
        c+=1

print(c)



