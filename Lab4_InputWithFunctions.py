# ENSF 692 Spring 2025
# May 15 Lab 4
# Input With Functions

# Add comments to explain the functionality of this program


def get_user_input(n):
    entry = input("Please type any entry #" + str(n + 1) + ": ")
    return entry, type(entry)

def process_user_input(n, entry, type):
    print("This is entry #" + str(n + 1) + ":", entry)
    print("The type of entry #" + str(n + 1) + " is :", str(type))


print('\n' * 2)
num_of_repeats = 3
results = []
results_types = []

for i in range(num_of_repeats):
    a, b = get_user_input(i)
    results.append(a)
    results_types.append(b)

for i in range(num_of_repeats):
    process_user_input(i,results[i], results_types[i])

