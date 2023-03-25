# 9-1. Restaurant:
print('9-1. Restaurant:')

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self. cuisine_type=cuisine_type
        self.restaurant_name=restaurant_name

    def describe_restaurant(self):
        print('the name of the hotel is ',self.restaurant_name)
        print('the name of cuisine type is ',self.cuisine_type)
    def open_restaurant(self):
        print('Restaurant is open')



restaurant=Restaurant('Mirchi 360','FastFood')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.cuisine_type

# 9-2. Three Restaurants:
print('\n9-2. Three Restaurants:')
restaurant1=Restaurant('Mirchi 360','FastFood')
restaurant2=Restaurant('Mirchi','Pizza House')
restaurant3=Restaurant('Spicy','Fish Point')
print('restaurant1')
restaurant1.describe_restaurant()
print('\nrestaurant2')
restaurant2.describe_restaurant()
print('\nrestaurant3')
restaurant3.describe_restaurant()

# 9-3. Users:
print('\n9-3. Users:')
class User:
    def __init__(self,first_name,last_name,age,phone_number,dept_name):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.phone_number=phone_number
        self.dept_name=dept_name
    def  describe_user(self):
        print('The first name of the user is ',self.first_name)
        print('The last name of the user is ',self.last_name)
        print('The Full name of the user is ',self.first_name+self.last_name)
        print('The age of the user is ',self.age)
        print('The phone number of the user is ',self.phone_number)
        print('The dept name of the user is ',self.dept_name)

    def greet_user(self):
        print('Thankyou so much for coming',self.first_name+self.last_name)


user1=User('sumair','ali',19,3083499,'software engineering')
user2=User('sumair','ali',19,3083499,'software engineering')
print('\nuser1')
user1.describe_user()
user1.greet_user()
print('\nuser2')
user2.describe_user()
user2.greet_user()

#  9-4. Number Served:
print('\n9-4. Number Served:')
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self. cuisine_type=cuisine_type
        self.restaurant_name=restaurant_name
        self.number_served=0

    def describe_restaurant(self):
        print('the name of the hotel is ',self.restaurant_name)
        print('the name of cuisine type is ',self.cuisine_type)
    def open_restaurant(self):
        print('Restaurant is open')

    def set_number_served(self,number):
        self.number_served=number
    def  increment_number_served(self,increment):
        self.number_served+=increment

restuarnt=Restaurant('Bismillah','chines')
restuarnt.number_served=5
print(f'the resutarant has served {restuarnt.number_served} customers')
restuarnt.set_number_served(10)
print(f'the resutarant has served' +str(restuarnt.number_served)+'customers')
restuarnt.increment_number_served(20)
print(f'the resutarant has served {restuarnt.number_served} customers')
