# 10-1. Learning Python:
print('10-1. Learning Python:')
filename = 'python.txt'

with open('python.txt') as file_object:
    contents = file_object.read()
    print(contents)

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# 10-2. Learning C:
print('10-2. Learning C: ')
with open(filename) as file_object:
    for line in file_object:
        newwline=line.replace('python','R')
        print(newwline.rstrip())


