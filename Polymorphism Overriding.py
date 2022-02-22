
class A:
    def show(self):
        print("AAAAAA")
        
class B:
    def show(self):
        print("BBBBB")        
        # return A.show(self)
     
     
     
class C(B,A):
    def show(self):
       print("CCCC")
       return A.show(self)  
           
     
     
c=C()
c.show()
super(C,c).show()   
     
     
     
     
     
     
     
        
# a=A()
# a.show()  



# b=B()
# b.show()         
# #go to the Parent of  B and  its self is b, execute function show
# super(B,b).show()











