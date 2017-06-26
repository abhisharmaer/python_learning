
#%%
#This script is to demonstrate Python Lists.
#my_list = ['Mike', 'Trump', '9999999999']   #Defining, initializing a Global List
import sys
sys.path.append('D:\Sharma_Abhishek\Learn\PythonPrj\PythonPrj')
import user_functions as uf
import shared_vars_constants as sc

#Printing Demo List with different parameters using overloaded function
#print_demo_list(params..)
uf.print_demo_list()
uf.print_demo_list("Printing Comments only")
uf.print_demo_list('My Demo List: ', sc.my_list)        
uf.print_demo_list('First Name is: ', sc.my_list, 0)    

#Adding a new item in list at a given index.
sc.my_list.insert(0,'Mr.')
uf.print_demo_list('My List with Salutation added at 0 index is: ', sc.my_list)

##Adding a new item with append method.
sc.my_list.append(['Male', 'Professional'])
print('My List with some items appended is: ', sc.my_list)

##Adding a new item with extended method.
print(sc.my_list.pop(len(sc.my_list) - 1))
sc.my_list.extend(['Male', 'Professional'])
print('My List with some items extended is: ', sc.my_list)

#Removing a specific item with another
uf.print_demo_list(uf.replace_item("Mr.", "Dr.",sc.my_list))

#To concatenate a list with another list.
copy_list = sc.my_list.copy()
copy_list.reverse()
uf.print_demo_list("List concatenated with reversed copy of my_list is: ", sc.my_list + copy_list)

#To repeat a list.
uf.print_demo_list("Printing My List with repeatition: ", 2 * sc.my_list)

my_list2 = 2 * sc.my_list

uf.rem_item_occurance('Mike',True,None,my_list2)
uf.rem_item_occurance('Trump',False,0,my_list2)
uf.rem_item_occurance('Dr.',False,0,my_list2)

sc.my_list.clear()
my_list2.clear()
#print(my_list2) ; print(sc.my_list)


#TODO: To implement List as Stack, Queues
#TODO: List Comprehensions,  Nested List Comprehensions
