'''
Create a class and object: Student details
Create a student class to store a student's name and roll number. Create an object and display the details using an instance method
'''

class std:
    def __init__(self, name, roll):
        self.n=name
        self.r=roll

    def display(self):
        print("Name = ",self.n)
        print("Roll No = ",self.r)

s1=std("Aks", 21)
s1.display()

