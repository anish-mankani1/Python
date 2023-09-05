class A:
    def display():
        print("display from A class")
class B(A):
    pass
   # def display():
    #    print("display from B class")
class C(A):
    pass
    #def display():
     #   print("display from C class")
class D(B,C):
    pass
   # def display():
    #    print("display from D class")
a=D
a.display()