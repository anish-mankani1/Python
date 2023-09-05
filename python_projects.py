print("*********************************")
print("welcome to my quiz")
questions=[
    {"text":" Who invented OOP?","answer":"c"},
    {"text":"Which feature of OOP indicates code reusability?","answer":"d"},
    {"text":"How many types of access specifiers are provided in OOP (C++)?","answer":"b"},
    {"text":"In multilevel inheritance, which is the most significant feature of OOP used?","answer":"d"},
    {"text":"Which of the following is not true about polymorphism?","answer":"b"}
]
options=[
    ["a.Andrea Ferro,b.Adele Goldberg,c.Alan Kay,d.Dennis Ritchie"],
    ["a.Abstraction,b.Polymorphism,c.Encapsulation,d.Inheritance"],
    ["a.4,b.3,c.2,d.1"],
    [" a.Code efficiency,b.Code readability,c.Flexibility,d.Code reusability"],
    ["a.Helps in redefining the same functionality,b.Increases overhead of function definition always,c.It is feature of OOP,d.Ease in readability of program"],
]
score=0
def check_answer(guess,questions_answer):
    if(guess==questions_answer):
        return True
    else:
        return False
for i in range(len(questions)):#5 0 1 2 3 4
    print("******************************")
    print(questions[i]["text"])#question ka o index par text print hoga
    print("tell your answer")
    for j in options[i]:#index 0 hai j mein options hai
        print(j)
        guess=input("enter the answer a/b/c/d")
        right_answer=check_answer(guess,questions[i]["answer"])
        print(right_answer)
        if(right_answer==True):
           print("correct answer")
           score+=1
        else:
         print("wrong answer")
        print(f"the correct answer is {questions[i]['answer']}")

print(f"your final score is{score}")