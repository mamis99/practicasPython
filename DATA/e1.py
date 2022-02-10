'''file = open('files/another_folder/my_file.txt')
content = file.read()
#print(content)
file.close()'''


#second way to read a file
with open('files/another_folder/my_file.txt') as file:
    content = file.read()
    print(content)

with open('files/another_folder/my_file.txt', mode='w') as file:
    #mode a = append
    #mode w = write
    #mode r = read
    file.write('THis is new to test my write mode')