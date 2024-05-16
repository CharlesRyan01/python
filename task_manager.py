#=====importing libraries===========
'''This is the section where you will import libraries'''

#====Login Section====
login=[]
with open("user.txt","r") as file:
    for line in file:
        name,password=line.rstrip().split(",")
        info={"name":name,"password":password}
        login.append(info)

jina=input("Enter name:")
siri=input("Enter password:")
for info in login:
    one=info["name"]
    two=info["password"]
    if (one==jina and siri==two):
         print("success")

while True:
    # Present the menu to the user and 
    # make sure that the user input is converted to lower case.
    menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
:''').lower()

    if (menu == 'r'):
            pass
            new=input("Enter name:")
            diff=input("Enter password:")
            diff2=input("Confirm password:")
            if (diff==diff2):
                with open("user.txt","a") as file:
                    file.write(f"{new},{diff}\n")
            else:
                print("Incorrect password try again")

    elif menu == 'a':
            pass
            name=input("Enter name:")
            title=input("Enter title:")
            desc=input("Enter description:")
            date=input("Input current date:")
            duedate=input("Input the due date:")
            complete=input("Is the task completed:")
            with open("tasks.txt","a") as file:
                file.write(f"{name},{title},{desc},{date},{duedate},{complete}\n")


    elif menu == 'va':
            pass
            container=[]
            with open("tasks.txt","r") as file:
                for lines in file:
                    name,title,desc,date,duedate,complete=lines.strip().split(",")
                    widow={'name':name,'title':title,'desc':desc,'date':date,'duedate':duedate,'complete':complete}
                    container.append(widow)

            for widow in container:
                print(widow)

    elif menu == 'vm':
        retwa=input("Enter name:")
        pass
        container=[]
        with open("tasks.txt","r") as file:
            for lines in file:
                name,title,desc,date,duedate,complete=lines.strip().split(",")
                widow={'name':name,'title':title,'desc':desc,'date':date,'duedate':duedate,'complete':complete}
                container.append(widow)

        for widow in container:
            site=widow['name']
            if (retwa==site):
                print(widow['title'],widow['desc'],widow['date'],widow['duedate'],widow['complete'])

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")
