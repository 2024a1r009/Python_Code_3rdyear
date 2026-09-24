# WAP to check whether  a no is perfect no. A no. is perfect if the sum of its proper divisor is equal to the no. itself
num = int(input("Enter the number : "))
sums = 0
for i in range(1,num):
  if num % int(i)== 0:
    sums+=i

if num==sums:
  print("Number is perfect number")
else:
  print("Number is not perfect number")