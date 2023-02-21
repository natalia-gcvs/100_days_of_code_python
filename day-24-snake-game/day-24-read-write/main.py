with open("C:/Users/User/Desktop/my_file.txt") as file:
    content = file.read()
    print(content)

with open('new_file.txt', mode='w') as file:
    file.write('I want to be wonderful')