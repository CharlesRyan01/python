'''mew="rob"
def hello():
    try:
        print(mew)
    except:
        print("mew is not defined")
    else:
        print("Hello rob")
    finally:
        print("good day")
hello()'''

age=17

if (age<18):
    raise Exception("Not today monkey")
else:
    print("hello person")