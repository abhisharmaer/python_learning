#%%
#This script is to demonstrate Python Lists.

my_list = ['Mike', 'Trump', '9999999999']   #Defining, initializing List
print('First Name: ', my_list[0])           #Printing 1st item in list.
print('Last Name: ', my_list[1])            #Printing 2nd item in list.
print('Mobile Name: ', my_list[2])          #Printing 3rd item in list.
print("Length of my list: " , len(my_list))

#Adding a new item in list at a given index.
my_list.insert(0,'Mr.')
print('My List with Salutation added at 0 index is: ', my_list)

#Adding a new item with append method.
my_list.append(['Male', 'Professional'])
print('My List with some items appended is: ', my_list)

#Adding a new item with extended method.
my_list.pop(len(my_list) - 1)
my_list.extend(['Male', 'Professional'])
print('My List with some items extended is: ', my_list)

#Remove a specific item from list with another.
#for i in range(len(my_list)):
#    if my_list(i) == 'Mr.':
#        my_list[i] = 'MR.'
#        print('My List with replacement is: ', my_list)
#    else:
#        print('My List without any replacement is: ', my_list)

#Printing list after removal of an item from index 2.

#To concatenate a list with another list.

#To repeat a list.


