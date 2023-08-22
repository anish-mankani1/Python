student_data=[
    {'name':'ram',"roll_no":26,"Age":26,"course":"python"},
    {'name':'mohan',"roll_no":26,"Age":26,"course":"python","phone_no":[1234,5678]}
]
def add(name,roll_no,course):
    new_list={}
    new_list["name"]=name
    new_list["roll_no"]=roll_no
    new_list["course"]=course
    student_data.append(new_list)

add("shyam",26,"c++")
print(student_data)
