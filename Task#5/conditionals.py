# 5-1. Conditional Tests:
print('5-1. Conditional Tests:')
name1='sumair'
name2='Basit'
print('Is name1==sumair ? i predict true')
print(name1=='sumair')
print('Is name1==Sumair ? i predict False')
print(name1=='Sumair')

print('Is name2==sumair and name1=Basit? i predict false:')
print(name1=='Basit' and name2=='sumair')

print('Is name2==sumair Or name1=Basit? i predict false:')
print(name1=='Basit' or name2=='sumair')

print('Is name2!=sumair Or name1!=Basit? i predict True:')
print(name1!='Basit' or name2!='sumair')

print('Is name2!=sumair and name1!=Basit? i predict True:')
print(name1!='Basit' and name2!='sumair')

# 5-2. More Conditional Tests:
print('\n\n5-2. More Conditional Tests:')
name3='khaliq'
name4='bilal'
name5='Bilal'
print(name3==name4)
print(name4==name5.lower())

print(5>9)
print(5<9)
print(5==9)
print(5!=9)
print(5 ==5 and 5==6)
print(9==9 or 5==9)

list=[10,5,7,8]
if 10 in list:
    print('yes {} is in the list'.format(10))
else:
        print('element not exist')



