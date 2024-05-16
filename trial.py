'''n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
n3=int(input("Enter third number:"))
total=n1+n2+n3

print(total)'''

'''name=input("Enter name:").lower()

if(name=="john"):
    print(f"{name} is a much")
else:
    print(f"No can do")'''


'''name= input("Enter student name:")
grade= input("Enter student grade:")

result=input(f"{name} has a {grade}")

print(result)'''

'''def total(num1,num2):
    print(num1+num2)

total(6,2)'''

'''numbers = [4,13,17,23]

for num in numbers:
    if num > 1:
        for i in range(2,num):
             if (num % i) == 0:
                print(num, "is not a prime number")
            else:
                print(num, "is a prime number")
    else:
         print(num, "is not a prime number")'''


'''students=[
    ("John",100),
    ("Sarah",50),
    ("Cone",30),
    ("Mary",70),
]

for total in students:
    for marks in total:
        mark=total[1]
        name=total[0]
        if (mark==100):
            print(name,"You have an A")
            break
        elif(mark<80 and mark>59):
            print(name,'You have a B')
            break
        elif(mark<59 and mark>49):
            print(name,'You have a c')
            break
        elif(mark<49 and mark>29):
            print(name,'You have a D')
            break'''

person={
    "name":"John Doe",
    "age":"45",
    "spouse":"Jane Doe",
    "occupation":"Lawyer",
    "hobbies":["Running","Chess","Rugby"],
    "car":{

    }
}
person['name']='Harry Kane'

print(person["hobbies"][2])