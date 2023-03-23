# 8-3. T-Shirt:
print(' 8-3. T-Shirt:')
def make_shirt(size,text_message):
    print('The size of T-shirt is ',size)
    print('The text written on T-shirt is',text_message)


make_shirt('small','Programmer`s have no life')
print('calling function using keyword argument:')
make_shirt(size='small',text_message='Programmer`s have no life')

# 8-4. Large Shirts:
print('8-4. Large Shirts:')
def make_large_shirt(size='large',text_message='i love python'):
    print('the size of shirt is ',size)
    print('the message written on shirt is',text_message)


make_shirt(size='medium',text_message='i love pyhton')

# 8-5. Cities:
def describe_city(city,country='pakistan'):
    print(city+' is in '+country)


describe_city(city='islamabad')
describe_city(city='delhi')
describe_city(city='madina')