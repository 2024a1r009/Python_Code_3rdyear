# WAP to check whether a given value is present in a tuple.If present, display its position 
# t=(1,2,3,"Apple", "bat", "rat")
# n=input("Enter the value : ")
# pos=0
# for i in range(len(t)):
#     if str(t[i])==n:
#         pos=i
#         break
# print(pos)        
t = (1, 2, 3, "Apple", "bat", "rat")

n = input("Enter the value: ")

for i in range(len(t)):
    if str(t[i]) == n:
        print(i)
        break
else:
    print("Not found")
