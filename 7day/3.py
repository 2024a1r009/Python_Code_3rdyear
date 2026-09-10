# wap to input two nos and find the GCD using a loop. 
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
while num2!=0:
  remainder = num1%num2
  num1 = num2
  num2 = remainder

print("GCD: ",num1)
