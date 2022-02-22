
class A:
    def show(self):
        print("AAAAAA")
        
class B(A):
    def show(self):
        print("BBBBB")        
        
        
a=A()
a.show()  

b=B()
b.show()         

super(B,b).show()