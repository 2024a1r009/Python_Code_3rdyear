# Take std full name and roll no. Generate email using first 3 letters of first name, first 3 letters of last name, and last 3 chars of roll ns
f=input("Enter full name: ")
n=input("Enter roll no : ")

space=f.find(" ")
first=f[:space]
last=f[space+1:]
email=first+last+n[:-3]+"@mietjammu.in"
print(email)



