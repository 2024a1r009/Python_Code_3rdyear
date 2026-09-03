# wap to take a word and count the no of vowels a,e,i,o,u
s=input("Enter your word: ")
c=0
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        c+=1

print(c)
