class rect:
    def __init__(self, len, bre):
        self.l=len
        self.b=bre

    def area(self):
        a=self.l*self.b
        print(a)

    def per(self):
        print(2*(self.l+self.b))    

    

r=rect(2,2)
r.area()
r.per()
