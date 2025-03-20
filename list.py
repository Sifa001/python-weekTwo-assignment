# creating a list
my_list = []

#appending elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#inserting a value to the list
my_list.insert(1,15)

#extending the list
my_list.extend([50,60,70])

#removing an item from the list
my_list.pop()

#sorting the list in ascending order
my_list.sort()

#finding and printing the index of 30
indexOf30 = my_list.index(30)
print(indexOf30)

print(my_list)
