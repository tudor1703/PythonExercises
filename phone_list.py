import sys

argv = sys.argv[1]

def list_func():
    with open('phone.txt', 'r') as t:
        for line in t:
            print(line.rstrip())
def phone_func1():
    with open ('phone.txt', 'r') as k:
        g = k.readlines()
        g.pop(2)
    print(g)
    with open('phone.txt', 'w') as c:
        c.write(' '.join(str(ln) for ln in g ))

def new_func():
    with open('phone.txt', 'w') as f:
        f.write(' '.join(str(nr) for nr in new_phone ))
        '''f.write(str(new_phone))'''
    print('A new object has been successfully saved!')      

if argv == 'insert':
    fname = input('enter the first name: ')
    lname = input('enter the last name: ')
    phone_num = input('enter the phone number: ')
    new_phone = [fname + '\n',lname + '\n',phone_num]
    new_func()

elif argv == 'list':
    list_func()

elif argv == 'delet':
    phone_func1()




