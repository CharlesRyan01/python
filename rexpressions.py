import re

with open("sample-2.txt","r") as f:
    file = f.read()
    
phone_regex=(r"\(\d{3}\) \d{3}-\d{4}")
email_regex=(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+")

numbers = re.finadall(phone_regex,file)
print(numbers)

email=re.findall(email_regex,file)
print(email)
# for line in file:
#         paper= line.rstrip()
#         blank.append(paper)

# if(re.search(pattern,pap)):
#     print(pap)
# else:
#     print("Invalid email")