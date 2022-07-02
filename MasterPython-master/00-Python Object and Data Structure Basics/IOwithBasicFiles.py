# How to perform simple I/O with basic.txt files
myfile = open('C:\\Users\\sanmaury\\Downloads\\Nordea-Training\\KT_Session1.txt')
content = myfile.read()
print(content)

# if yiu want to read the file again reset the cursor to 0
myfile.seek(0)
content = myfile.read()
print(content)

# if you want to reead each line and result in list
myfile.seek(0)
content = myfile.readlines()
print(content)

#close the file
myfile.close()
# latest way of reading/writing a file
with open('C:\\Users\\sanmaury\\Downloads\\Nordea-Training\\misc\\test.txt', mode='r') as my_test_file:
    contents = my_test_file.read()
print(contents)

# Appending to an existing file
with open('C:\\Users\\sanmaury\\Downloads\\Nordea-Training\\misc\\test.txt', mode='a') as my_test_file:
    my_test_file.write('3.I am fine, what about you?')

# read after writing
with open('C:\\Users\\sanmaury\\Downloads\\Nordea-Training\\misc\\test.txt', mode='r') as my_test_file:
    read_again = my_test_file.read()
print(read_again)