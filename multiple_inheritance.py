#mummy papa and son
class human:
    def eat():
        print("i can eat")
    def work():
            print("i can work")
class male:
    def flirt():
        print("i can flirt")
    def work():
            print("i can code")
class boy(human,male):
    def run():
         print("i can run")
    def work():
         print("i can test")
boy_1=boy
boy_1.eat()
boy_1.flirt()
boy_1.work()# yaha code isliye print nahi huha kyu ki humne argument mein pehle human 
#pass kiya pehle jo pass karege uski pehli priritory hogi
print(boy_1.mro()) # yeh function sequence bata hega humko kauns pehele hai