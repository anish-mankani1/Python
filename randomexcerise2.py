import random
names=input("enter names separated by comma")
names_list=names.split(",")
print(names_list)
lenght=len(names_list)  # yaha se length pata padi
random_list=random.randint(0,lenght-1)  #jaise length 3 hai par index 0 se chalu hota hai
#isliye aisa kiya
print(f" {names_list[random_list]} will pay the bill")
