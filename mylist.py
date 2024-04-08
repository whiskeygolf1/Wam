my_list = []
print(my_list)
#append individual elements to my_list
my_list.extend([10, 20, 30, 40])
my_list.insert(1, 15)
#extend my_list with another list
my_list.extend([50, 60, 70])
#remove the last element
my_list.pop(-1)
#sort my_list in ascending order
my_list.sort()
#find and print the index of the value 30 in my_list
print(my_list.index(30))