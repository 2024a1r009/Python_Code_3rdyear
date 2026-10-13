
# l=list(map(int,input().strip().split()))
# m=l[0]
# for i in l:
#     if i>m:
#         m=i


# print(m)
# t=[]
# for i in l:
#     if i!=m:
#         t.append(i)

# m1=t[0]
# for i in t:
#     if i>m1:
#         m1=i        
# print(m1)


# Prime or not 
# p=0
# n=int(input("e="))
# for i in range(3,n):
#     p=1
#     for j in range(2,i):
#         if i%j==0:
#             # print("Not prime")
#             p=0
#             break
        
#     else:
#         print(i)           

# palindrome
# l=[]
# n=input("Enter = ")
# for i in range(len(n)):
#     n=int(n)
#     p=n%10
#     l.append(p)

#     n=n//10

# for i in l:
#     print(i,end="")

# l=[]
# r=0
# n=input("Enter = ")
# for i in range(len(n)):
#     n=int(n)
#     p=n%10
#     r=r*10+p
    

#     n=n//10

# print(r)

# armstrong 
# s=0
# n=input("Enter = ")

# l=len(n)
# n1=int(n)
# for i in range(l):
#     n=int(n)
#     p=n%10
#     t=p**l
#     s+=t
    
    

#     n=n//10

# if s==n1:
#     print("yes")
# else:
#     print("No")    

# n=int(input("E: "))
# dict={}
# for i in range(n):
#     n=input("n:  ")
#     m=int(input("m: "))
#     dict[n]=m

# print(dict)
# dict={'A': 80, 'B': 90, 'C': 75}
# # for key, value in dict.items():
# #     print(f"{key}: {value}")
# for key in dict:
#     print(key)

# s="akshra"
# d={}
# for i in s:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1

# print(d)            

# d = {"A": 10, "B": 20, "C": 30}
# s=0
# for key,value in d.items():
#     s+=value
# print(s)   
#  
# u=0
# for key,value in d.items():
#     if value > u:
#         u=value
# print(u)        
# print(d[0])
# d={}
# l=["apple","mango" ,"apple" ,"banana" ,"mango" ,"apple"]
# for i in l:

#         if i not in d:
#             d[i]=1
#         else:
#             d[i]+=1

# print(d)                
    
# d1 = {"a": 10, "b": 20}
# d2 = {"b": 50, "c": 30}

# for key,value in d2.items():
#     if key not in d1:
#         d1[key]=value
#     else:
#         d1[key]=d1[key]+d2[key] 
# print(d1)    


# class std:
#     def __init__(self, name, age):
#         self.n=name
#         self.a=age

#     def d(self):
#         print(self.n,self.a)

# s1=std("aks",12)
# s1.d()
s="aks"

for i in s:
    t