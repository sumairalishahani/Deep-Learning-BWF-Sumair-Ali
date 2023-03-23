# 7-1. Rental Car:
rental_car=input("what kind of rental car you would like?")
print('let me see if i can found you a ',rental_car)

# 7-2. Restaurant Seating:
count_people=input("how many people are in your dinner group?")
if int(count_people)>8:
    print("they’ll have to wait for a table.")
else:
    print('their table is read:')

# 7-3. Multiples of Ten:
numbers=input("Enter any number you would like:")
if int(numbers)%10==0:
    print(numbers,'the number is multiple of 10:')
else:
    print(numbers,'is not multiple of 10:')