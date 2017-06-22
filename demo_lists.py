#%%
#This script is to demonstrate Python Lists.
my_list = ['Mike', 'Trump', '9999999999']   #Defining, initializing a Global List

#Defining print_demo_list as overloaded function.
def print_demo_list(comment=None,demolist=None,index=None):      
    
    if index is None and demolist is None and comment is None:
        print("Blank, No Arguments provided")
    elif index is None and demolist is None and comment is not None:
        print(comment)
    elif index is None and demolist is not None:
        print(comment,demolist)
    elif index is not None:
        print(comment,demolist[index])
   
#Printing Demo List with different parameters using overloaded function print_demo_list(params..)
print_demo_list()
print_demo_list("Printing Comments only")
print_demo_list('My Demo List: ', my_list)        
print_demo_list('First Name is: ', my_list, 0)

#Adding a new item in list at a given index.
my_list.insert(0,'Mr.')
print_demo_list('My List with Salutation added at 0 index is: ', my_list)

##Adding a new item with append method.
my_list.append(['Male', 'Professional'])
print('My List with some items appended is: ', my_list)

##Adding a new item with extended method.
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


