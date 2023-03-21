import sys

argv = sys.argv[1]

def list_func():
    with open('phone.txt', 'r') as t:
        for line in t:
            print(line.rstrip())

def new_func(new_phone):
    with open('phone.txt', 'w') as f:
        f.write(str(new_phone))
    print('A new object has been successfully saved!')

if argv == 'insert':
    fname = input('enter the first name: ')
    lname = input('enter the last name: ')
    phone_num = input('enter the phone number: ')
    new_phone = fname, lname, phone_num
    new_func(new_phone)

elif argv == 'list':
    list_func()

