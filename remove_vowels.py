string=input("enter a sentence")
vowels=['a','e','i','o','u','A','E','I','O','U']
result=""
for x in range(0,len(string)):
    if string[x] not in vowels:
        result+=string[x]

print(result)

