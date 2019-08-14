'''
Demonstrate the use of the .enumerate() function.
'''

list_of_things = ["Dog", "Chair", "Boat", "chicken", "other things"]

for i, thing in enumerate(list_of_things, start=1):
    print(f"{i}: {thing}")

