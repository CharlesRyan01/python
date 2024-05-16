#create user
name= input("Enter your name:")
email=input("Enter your email:")
id=input("Enter your ID number:")
with open("wompwomp.txt","a") as file:
    file.write(f"{id},{name},{email},True\n")

#