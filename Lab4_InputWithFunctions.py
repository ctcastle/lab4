# ENSF 692 Spring 2025
# May 15 Lab 4
# Input With Functions

# Add comments to explain the functionality of this program

# Function that retrieves user input from terminal using the Python 'input' command 
def get_user_input(n):
    entry = input("Please type any entry #" + str(n + 1) + ": ")
    return entry, type(entry)

def process_user_input(n, entry, type):
    print("This is entry #" + str(n + 1) + ":", entry)
    print("The type of entry #" + str(n + 1) + " is :", str(type))

#Program starts here, adds 2 blank lines in user's console 
print('\n' * 2)
#Set value of variable to 3, this should be an int 
num_of_repeats = 3
#Create 2 empty lists for storing values for the results of the program output  
results = []
results_types = []
#Start a for loop that will iterate from 0 to 1-num_of_repeats, which is 3 in this example 
#this uses the function range(end) which produces a range object which produces a sequence of integers from the start (default 0) inclusive, 
#to the end value exclusive. In this example it produces a range object that would have the sequence of integers 0,1,2 
for i in range(num_of_repeats):
    #Calls a function that outputs some entry from a user (stored in variable a) as well as the type of the output (stored in variable b)  
    a, b = get_user_input(i)
    #The value is stored in the results list, added to the end of the list 
    results.append(a)
    #The type of the value is stored in this list, added to the end of the list 
    results_types.append(b)
#Start a for loop that will iterate from 0 to 1-num_of_repeats, which is 3 in this example 
#this uses the function range(end) which produces a range object which produces a sequence of integers from the start (default 0) inclusive, 
#to the end value exclusive. In this example it produces a range object that would have the sequence of integers 0,1,2 
for i in range(num_of_repeats):
    #Calls a function that prints out the results and result types in a neatly formatted way 
    process_user_input(i,results[i], results_types[i])

