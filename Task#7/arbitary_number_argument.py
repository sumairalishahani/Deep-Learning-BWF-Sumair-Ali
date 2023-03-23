# 8-12. Sandwiches:
print('8-12. Sandwiches:')
def make_sandwich(*items):
    print('making a sandwich with following items:\n',items)


make_sandwich('vegetables','meat')
make_sandwich('vegetables','sliced','chesse')
make_sandwich('vegetables','sliced','chesse','meat')

# 8-13. User Profile:
print('8-13. User Profile:')
def build_profile(first, last, **user_info):
 """Build a dictionary containing everything we know about a user."""
 profile = {}
 profile['first_name'] = first
 profile['last_name'] = last
 for key, value in user_info.items():
     profile[key] = value
 return profile


user_profile = build_profile('Sumair', 'Ali',
 location='karachi pk',
 field='programer')
print(user_profile)


