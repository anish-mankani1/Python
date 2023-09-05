#human male female and transgender
class human:
    def sleep():
        print("you can sleep now")
class male(human):
    def eat():
        print("you can eat")
class female(human):
    def flirt():
        print("you can flirt")
fem_1=female
fem_1.flirt()
fem_1.sleep()
male_1=male
male_1.eat()
male_1.sleep()
