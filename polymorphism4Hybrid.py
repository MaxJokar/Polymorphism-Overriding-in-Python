#Hybrid inheritance:
class A:
    def show(self):
        print("AAAAAA")
        
class B(A):
    def show(self):
        print("BBBBB") 
        return A.show(self)       
     
     
     
 #  Priority is with  B  first C goes to B then A :    
class C(A):
    def show(self):
       print("CCCC")
       return B.show(self) 
      
           
class D(B,C):
    def show(self):
       print("DDDDDD")
       return C.show(self) 
d=D()
# d.show()
super(D,d).show()

    

     