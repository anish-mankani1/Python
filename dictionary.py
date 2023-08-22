#dictionary are used key and keyvalue
phone_no={'ram':1234,'shyam':'5678','mohan':'1234','ram':6666}
#duplicate are not allowed by default it will consider last value assign to it
print(phone_no)
print(phone_no['shyam'])
phone_no['mohan']=9999 #we can also change values
print(phone_no)
phone_no['madhav']={1111,2222,3333}
print(phone_no)
phone_no['shyam']={'shyam_home':7777,'shyam_work':8888}
print(phone_no)
print(phone_no['shyam']['shyam_work'])
print(phone_no.get('ram'))#we can also access by get method
print(phone_no.get("Ram"))#  capital R it will not give eerror other then it will print none
data={
    1:'jenny',
    2:'shyam',
    0:'mohan'
}
del phone_no['ram']
print(phone_no)
print(data[0])
print(phone_no.pop('shyam'))
print(phone_no)
print(phone_no.keys())#we can aceess only values keys and item
print(phone_no.values())
print(phone_no.items())
for i in phone_no:
    print(i)# it will only print keys
    print(phone_no[i])# to acees value we use phone number)
    phone_no2=phone_no.copy()
    print(phone_no2)
    print(len(phone_no))
