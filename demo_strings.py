#%%
#This script is to demonstrate Strings and operations on Strings.

#Defining String variables and assiging values.

name = "Abhishek Sharma"
print("My name is: " , name)

#Subsets of strings using slice operator ([ ] and [:])

print("First Name: " , name[0:8])
print("Last Name: " , name[9:])

#Subsets of strings using slice operator ([ ] and [:]) and processing with -ve index
print("First Name as processed from right to left:" , name[-15:-7])
print("Last Name as processed from right to left:" , name[-6:])

msg = 'Hello World!'
print("First character of msg is: ", msg[0])
print("Last character of msg is: ", msg[-1])

#Printing msg multiple times
print(2 * msg)

#Print msg concatenated with another msg.
print(msg + ' This is Python Strings Demo! :-)')

