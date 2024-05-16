num1=int(input("Input first number:"))
num2=int(input("Input second number:"))


while True:
    menu=input('''Select the operation:
a-addition       
s-subtraction
d-division
m-multiplication
h-history
:''')
    if(menu=='a'):
        result=num1+num2
        sign=str('+')
        print(result)

    elif(menu=='s'):
        result=num1-num2
        sign=str('-')
        print(result)

    elif(menu=='d'):
        sign=str('/')
        try:
            result=num1/num2
        except:
            raise Exception('Zero division error')
        else:
            print(result)

    elif(menu=='m'):
        result=num1*num2
        sign=str('*')
        print(result)

    elif(menu=='h'):
        values=[]
        with open("equation.txt","r") as file:
            for line in file:
                values.append(line.rstrip())
        print(values)

    else:
        print("Choose a given value")

    with open("equation.txt","a") as file:
        file.write(f"{num1}{sign}{num2}={result}\n")