
class A:
    def show(self):
        print("AAAAAA")
        
class B:
    def show(self):
        print("BBBBB")        
        return A.show(self)
     
     
 #  Priority is with  B  first C goes to B then A :    
class C(B,A):
    def show(self):
       print("CCCC")
       return B.show(self)  
           
     
     
c=C()
c.show()
print()
super(C,c).show()   
     
     
     
     
     
     
     
        
# a=A()
# a.show()  



# b=B()
# b.show()         
# #go to the Parent of  B and  its self is b, execute function show
# super(B,b).show()











