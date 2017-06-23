#%%
#This script is to demonstrate Python Lists.
my_list = ['Mike', 'Trump', '9999999999']   #Defining, initializing a Global List

#Defining print_demo_list as overloaded function.
def print_demo_list(comment=None,demolist=None,index=None): 
    #if index is None and demolist is None and comment is None:
    #    print("Blank, No Arguments provided")
    if index is None and demolist is None and comment is not None:
        print(comment)
    elif index is None and demolist is not None:
        print(comment,demolist)
    elif index is not None:
        print(comment,demolist[index])
   
#Replace a specific item from list with another using enumerate as iterator.
def replace_item(searchitem,replaceitem):
    for i, val in enumerate(my_list):
        if val == searchitem:
            my_list[i] = replaceitem
            print_demo_list('My List with replacement is: ', my_list)
            break
            return my_list
        else:
            print_demo_list('My List without any replacement is: ', my_list)
            return my_list

#Removing all occurances of an item in a list.
def rem_item_occurance(item=None,all_flag=None,index=None):    #TODO: how to have item as a list to remove multiple items at once?
    if all_flag == True:
        for i, val in enumerate(my_list2):
            if val == item:
                my_list2.remove(val)
                print("Item", item,"removed from index[",i,"]")
            else:
                print("Item",item,"not found in my_list2 @ index[",i,"]" )
        return(my_list2)
    else:
        for i, val in enumerate(my_list2):
            if val == item:
                my_list2.pop(index)
                print("Item found and removed at index[",i,"] \n",my_list2)
                break
            else:
                print("Item to be removed not found at index: [",i,"]")
        #return(my_list2)


#Printing Demo List with different parameters using overloaded function
#print_demo_list(params..)
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
print(my_list.pop(len(my_list) - 1))
my_list.extend(['Male', 'Professional'])
print('My List with some items extended is: ', my_list)

#Removing a specific item with another
print_demo_list(replace_item("Mr.", "Dr."))

#To concatenate a list with another list.
copy_list = my_list.copy()
copy_list.reverse()
print_demo_list("List concatenated with reversed copy of my_list is: ",my_list + copy_list)

#To repeat a list.
print_demo_list("Printing My List with repeatition: ", 2 * my_list)

my_list2 = 2 * my_list
rem_item_occurance('Mike',True)
rem_item_occurance('Trump',False,0)
rem_item_occurance('Dr.',False,0)


