# 3-4. Guest List:

guests=['sumair','masood','basit']
for guest in guests:
    print('i would like to invite '+guest+",\nin my dinner party")

# 3-5. Changing Guest List:

print(guests[2]+"\n\n oh is not coming because of emergency")
guests[2]='ali'
for guest in guests:
    print('i would like to invite'+guest+",\nin my dinner party")
    print(guest)


# 3-6. More Guests:
print('\nI found a bigger dinner table\n')
guests.insert(0,'Ahmed')
guests.insert(2,'Uzair')
guests.append('Muzamil')
for guest in guests:
    print('so Now i would like to invite'+guest+",\nin my dinner party")

# 3-7. Shrinking Guest List:
print('\n i can only invite two people for dinner\n')
while len(guests)>2:
    removed_person=guests.pop()
    print("Sorry " + removed_person + ", I can't invite you to the dinner.")

for guest in guests:
    print("Dear " + guest + ",\nYou are still invited to a dinner party a")

del guests[1]
del guests[2]
print(guests)