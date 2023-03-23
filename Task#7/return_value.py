# 8-6. City Names:
print('8-6. City Names:')
def city_country(country,city):
    return country.title()+','+city.title()


print(city_country('"pakistan','karachi"'))
print(city_country('"india','mumbai"'))
print(city_country('"saudiArabia','madina"'))

# 8-7. Album:
print('8-7. Album:')
def make_album(artist_name,album_title):
    music_album={'artist_name':artist_name,'album_title':album_title}
    return music_album


print(make_album('sumair ali','programers have no life'))
print(make_album('sumair ali','python is my life'))
print(make_album('sumair ali','programers have no life'))


