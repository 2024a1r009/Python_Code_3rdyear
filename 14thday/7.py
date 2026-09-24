# WAP  to tsore multiple student records as a list of tuple. 
# Each tuple should contain name, roll no, and marks. Display students who scord above 75.
t=(["sabrina",1,99],["rom", 2,64],["jav", 44,35],["rav", 44,78])
l=[]
# print(t[0][2])
for i in range(len(t)):
    if t[i][2]>75:
        l.append(t[i][0])

print(l)

