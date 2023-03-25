
# 9-6. Ice Cream Stand:
print('9-6. Ice Cream Stand:')
class Restaurant(object):
    def __init__(self, restaurant_name, cuisine_type):
        self. cuisine_type=cuisine_type
        self.restaurant_name=restaurant_name

    def describe_restaurant(self):
        print('the name of the hotel is ',self.restaurant_name)
        print('the name of cuisine type is ',self.cuisine_type)
    def open_restaurant(self):
        print('Restaurant is open')


class  IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors=['vinila','straberry','coclate']
    def display_flavours(self):
        for i in self.flavors:
            print('the flavours of icecreame is ',i)

icecream=IceCreamStand('spicy','fishpoint')
icecream.display_flavours()

# 9-7. Admin:
print('\n 9-7. Admin:')


class User:

    def __init__(self, first_name, last_name, age, phone_number,dept):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number
        self.dept=dept

    def describe_user(self):

        print('First Name:', self.first_name)
        print('Last Name:',self.last_name)
        print('Age:',self.age)
        print('phone_number:',self.phone_number)
        print('dept:',self.dept)

    def greet_user(self):
        print('welcome'+self.first_name+self.last_name)



class Privileges:

    def __init__(self):

        self.privileges = ["can add post", "can delete post", "can ban user"]
    def show_privileges(self):
        print('Privileges',self.privileges)


class Admin(User):
    def __init__(self, first_name, last_name, phone_number, dept):
        super().__init__(first_name, last_name, phone_number, dept)
        self.privileges = Privileges()


#admin = Admin('Sumair','Ali',20,3333,'sw')
#admin.privileges.show_privileges()


# 9-9. Battery Upgrade:
print('\n 9-9. Battery Upgrade:')


class Car:

    def __init__(self, make, model, year):

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = self.year+self.make+self.model
        return long_name.title()

    def read_odometer(self):
        print('This car has'+str(self.odometer_reading)+'miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can not back")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:


    def __init__(self, battery_size=75):

        self.battery_size = battery_size

    def describe_battery(self):

        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):

        if self.battery_size == 75:
            range = 100
        elif self.battery_size == 85:
            range = 160

        print('This car can go about'+str(range)+ 'miles on a full charge.')

    def upgrade_battery(self):

        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):
    def __init__(self, make, model, year):

        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("This car doesn't need a tank")



civic = ElectricCar('cicic', 'model c', 2020)

civic.battery.get_range()

civic.battery.upgrade_battery()
civic.battery.get_range()
