import sys

arg = sys.argv[1]

if arg == '1':
    fname = input('enter the first name: ')
    lname = input('enter the last name: ')
    phone_num = input('enter the phone number: ')
    new_phone = fname, lname, phone_num
else:
    print('error')

def new_func(new_phone):
    with open('phone.txt', 'w') as f:
        f.write(str(new_phone))
    print('A new object has been successfully saved!')

new_func(new_phone)
