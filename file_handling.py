with open("words (1).txt","r")as file:
    file_content=file.readlines()

    for item in file_content:
        if(len(item)>9):
            print (item)