class a:
    def mama():
        print("mama")
class b:
    def chacha():
        print("chacha")
class c:
    def mausa():
        print("mausa")
class d(c,b):
    def mausi():
        print("mausi")
d1=d
d1.chacha()
d1.mausa()
d1.mausi()