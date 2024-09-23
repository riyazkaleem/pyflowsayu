
#writing contents into the file
with open("sec24filesystem/text.txt", mode="a") as file:
    file.write('new_text.')
    
#reading the contents of the file
with open("sec24filesystem/text.txt") as file:
    contents = file.read()
    print(contents)
    # print(contents)