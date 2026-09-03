s=input("Enter name: ")
b=input("Enter branch: ")
y=input("Enter year: ")
code=s[:3]+"-"+b[:3]+"-"+y[:4]
print(code)
print(code*3)