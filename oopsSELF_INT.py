class instructor:
    follower=0     #CLASS OBJECT VARIABLE
    def __init__(self,name,address) :
        self.name=name
        self.address=address

    def display(self,subject):# humko bracket mein self likhna padega imp hai
           print(f"hi my name is {self.name} and my favorite subject is {subject}")
instructor_1=instructor("anish","nagpur") # self name is attribute and subject is arugument
print(instructor_1.name) 
print(instructor_1.follower)   
instructor_1.display("python")     

    