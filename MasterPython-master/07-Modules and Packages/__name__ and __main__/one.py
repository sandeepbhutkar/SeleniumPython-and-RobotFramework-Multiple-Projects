
def func():
    print("I am func() in one.py")

print("Top Level in one.py")

if __name__ == '__main__':
    print("one.py is being run directly")
else:
    print("one.py has been imported")