#grandfather father and son
class human():#grand parent
    def fruit():
        print("you have my respect")
    def work():
       print("you have to work")
class male(human):#parent
    def sleep():
     print("you are male")
class boy(male):#child 1
   def sigma():
    print("you are a boy")
    def work():
     print("you are a coder")
class programmer(boy):#child 2
   def flirt():
      print("you can flirt ")
boy_1=boy
boy_1.fruit()
print(boy_1.mro())# pehle boy phir male phir male phir human phir object
#object class  kuch nahi khud ba khud define ho jata hai
#object class base class hoti hai sab class ki iske andar init function hota hai jenny