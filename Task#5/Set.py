set_of_list=set(['sumair','basit'])
print(set_of_list)
# set returns only unique values not repeadted
print('add method of set\n')
set_of_list.add('Bilal')
print(set_of_list)
set_of_list.add('Bilal')
print(set_of_list)
print('copy method of set\n')
set_of_list.copy();
print(set_of_list)

print("Remove method")
set_of_list.remove('Bilal')
print(set_of_list)

print('Pop method')
set_of_list.pop();

# Intersetion
print("\n\n Intersection of set")
A={3,4,5,7}
B={3,6,4,9}
X=A.intersection(B)
print(X)

# Union
print("\n\n Union of set")
A={3,4,5,7}
B={3,6,4,9}
X=A.union(B)
print(X)

# Symmetric Differnece
print("\n\n Symmetric Differnece of set")
A={3,4,5,7}
B={3,6,4,9}
X=A.symmetric_difference(B)
print(X)
