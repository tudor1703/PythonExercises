given_file = open('python.txt', 'r')

lines = given_file.readlines()
sum = 0

for line in lines:
    for c in line:
        if c.isdigit() == True:
            sum = sum + int(c)

print(sum)

given_file.close()