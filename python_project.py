def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
operation={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
first_number=int(input("enter first number"))
for symbol in operation:
    print(symbol)
operator=input("enter the operator")
second_number=int(input("enter second number"))
calculator=operation[operator]
output=calculator(first_number,second_number)
print(f"the first_number is{first_number} and second_number is{second_number}and operator is {operator} and result is {output}")