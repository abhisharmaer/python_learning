import shared_constants as sc

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
def replace_item(searchitem,replaceitem,locallist=None):
    for i, val in enumerate(locallist):
        if val == searchitem:
            locallist[i] = replaceitem
            print_demo_list('My List with replacement is: ', locallist)
            break
            return locallist
        else:
            print_demo_list('My List without any replacement is: ', locallist)
            return locallist

#Removing all occurances of an item in a list.
def rem_item_occurance(item=None,all_flag=None,index=None,list=None):    #TODO: how to have item as a list to remove multiple items at once?
    if all_flag == True:
        for i, val in enumerate(list):
            if val == item:
                list.remove(val)
                print("Item", item,"removed from index[",i,"]")
            else:
                print("Item",item,"not found in my_list2 @ index[",i,"]" )
        return(list)
    else:
        for i, val in enumerate(list):
            if val == item:
                list.pop(index)
                print("Item found and removed at index[",i,"] \n",list)
                break
            else:
                print("Item to be removed not found at index: [",i,"]")
        #return(my_list2)


