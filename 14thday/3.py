# WAP to show that tuple values cannot be changed directly. Convert tuple into list,
#  Update it, and convert it back into tuple 
t=("apple", "Banana", "Orange")

l=[]
for i in range(len(t)):
    l.append(t[i])

print("list: ", l)    

w=input("Update the list: ")
l.append(w)
print("Updated list: ", l)
z=tuple(l)
print(z)
print(type(z))



