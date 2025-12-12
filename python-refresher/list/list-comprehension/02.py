numbers = [1,23,3,4,5,6,6]
even = []

even = [ i for i in numbers if i % 2 == 0 ]

print(even)

fruits = ['orange','guava','pineapple']
new_item =[]

# for x in fruits:
#     if 'a' in x:
#         new_item.append(x)
#         print(new_item)

new_item = [x for x in fruits if 'a' in x ]
