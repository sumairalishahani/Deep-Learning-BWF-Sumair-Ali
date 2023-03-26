# 10-3. Guest:
print('10-3. Guest:')
filename='programer.txt'
with open(filename,'w') as file_object:
    user_name=input("your name plz:")
    file_object.write(user_name)

# 10-4. Guest Book:
print('10-4. Guest Book:')
while True:
        name = input('your name handsome:')
        if name=='quit':
            break
        else:
            filename = 'guest_book.txt'
            with open(filename, 'a') as file_object:
                print('welcome beautiful', name.title())
                file_object.write(f"{name.title()} visited the guest book.\n")


# 10-5. Programming Poll:
print('10-5. Programming Poll:')
while True:
    reason=input("why you like programming,or (enter quit to stop program)")
    if reason=='quit':
        break
    else:
        filename='programer_poll.txt'
        with open(filename,'a') as file_object:
            file_object.write(reason+"\n")
            print('thanks for your response')
