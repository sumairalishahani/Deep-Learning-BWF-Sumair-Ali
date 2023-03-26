# 10-6. Addition:
print('10-6. Addition:')
number1=input('Enter number 1:')
number2=input('Enter number 2:')
try:
    sum=int(number1)+int(number2)
except TypeError:
    print('you can not add string to integer')
else:
    print('sum:',sum)

# 10-8. Cats and Dogs:
print('\n10-8. Cats and Dogs:')
cat_filename = 'cats.txt'
dog_filename = 'dogs.txt'

try:
    with open(cat_filename) as cat_file:
        print('Contents of',cat_filename)
        for line in cat_file:
            print(line.rstrip())
except FileNotFoundError:
    print(f"{cat_filename} not found.")

try:
    with open(dog_filename) as dog_file:
        print(f"\nContents of {dog_filename}:")
        for line in dog_file:
            print(line.rstrip())
except FileNotFoundError:
    print(f"{dog_filename} not found.")

# 10-9. Silent Cats and Dogs:
print('\n10-9. Silent Cats and Dogs:')
try:
    with open(cat_filename) as cat_file:
        print('Contents of',cat_filename)
        for line in cat_file:
            print(line.rstrip())
except FileNotFoundError:
    pass
try:
    with open(dog_filename) as dog_file:
        print(f"\nContents of {dog_filename}:")
        for line in dog_file:
            print(line.rstrip())
except FileNotFoundError:
    pass
