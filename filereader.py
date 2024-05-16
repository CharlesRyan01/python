'''names=[]
with open("names.txt","r") as file:
    for line in file:
       names.append(line.rstrip())

for name in sorted(names):
    print(name)'''

#CSV Reader
books=[]
with open("books.csv","r") as file:
    for line in file:
      title,author,price= line.rstrip().split(",")
      book={"title":title, "author":author, "price":price}
      books.append(book)

for book in books:
    print(book)

jina=input("Enter author name:")

for book in books:
    change=book["author"]
    def get_author(change):
        if (jina==change):
            print(book["title"],book["price"])
    get_author(change)

small=input("Enter minimum price...")
big=input("Enter maximum price...")

for book in books:
    def get_price(book):
        amount=book["price"]
        if (amount>=small and amount<=big):
            print(book["title"],book["author"],book["price"])
    get_price(book)