#student_data={
 ##   "ram":{"roll_no":26,"Age":26,"course":"python"},
   # "mohan":{"roll_no":27,"Age":27,"course":"python"}
#}
#print(student_data)
#print(student_data["mohan"]["roll_no"])# we can  aceess
#student_data["mohan"]["phone_no"]=8378853372# we can add
#print(student_data["mohan"])
#del student_data["mohan"]["phone_no"]
#print(student_data["mohan"])
#print(student_data["mohan"].pop("course"))

#nested list in dictionary
#travel_data={
 #   "gujrat":['somnath','dwarka'],
  #  "rajasthan":['jaipur','udaipur']
#}
#print(travel_data)
#print(travel_data["rajasthan"])



#list under dictionary
student_data=[
    {'name':'ram',"roll_no":26,"Age":26,"course":"python"},
    {'name':'mohan',"roll_no":26,"Age":26,"course":"python","phone_no":[1234,5678]}
]
print(student_data)
print(student_data[0])
print(student_data[1]["phone_no"])