email=input("Enter: ")
sp=email.find("@")

user=email[:sp]
dom=email[sp+1:]
rev_d=dom[::-1]
print("Username: ",user)
print("Domain: ",dom)
print("Rev_Domain: ",rev_d)