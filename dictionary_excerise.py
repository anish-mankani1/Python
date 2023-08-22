student_marks={
    'jenny':92,
    'hemant':87,
    'rohit':77,
    'chinki':67,
    'kudi':55,
    'anish':44
}
student_grades={}
for i in student_marks:
    marks=student_marks[i]#92 assign to marks
    if(marks>90):
        student_grades[i]="A+"
    elif(marks>80):
        student_grades[i]="B+"
    elif(marks>70):
        student_grades[i]="c+"
    elif(marks>60):
      student_grades[i]="d+"
    elif(marks>50):
      student_grades[i]="e+"
    else:
      student_grades[i]="f+"
print(student_grades)

