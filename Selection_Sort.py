# Selection Sort

# List of unsorted numbers
list_of_num = [45, 27, 13, 98, 16, 104 ,20, 67, 73, 34 ]

# Display list of unsorted numbers
print("Unsorted")
for item in list_of_num:
    print(item)

# Get the how many numbers there is in the list
length = len(list_of_num)
# The number of sorted items
number_of_sorted_items = 0
# Initialize index values
# The index to start sorting from
index = 0
# The index of the smallest value
min_index = 0

# Run once the number of unsorted items is less than the number of items in the initial list
while number_of_sorted_items < length - 1:
    # Set the smallest current value to the value store at the current index
    current_minimun = list_of_num[index]
    
    # Go through the list of numbers
    for next_index in range(index, length):
        # Check if the number at the next index is less than the current smallest value
        if list_of_num[next_index] < current_minimun:
            # If true
            # Set the smallest value to the value at the current index
            current_minimun = list_of_num[next_index]
            # Set the smallest index the the current index
            min_index = next_index

    # After all the values are checked from the initial index
    # Create a temporary value for the value stored at the initial index
    temp = list_of_num[index]
    # Set the value at the initial index to the smallest value determined 
    list_of_num[index] = current_minimun
    # Set the value of the index where the smallest value was initially store to the value of the initial index
    list_of_num[min_index] = temp
    # Increase the initial index i.e. what index to start sorting from
    index += 1
    number_of_sorted_items += 1
    
print("\nSorted")
for item in list_of_num:
    print(item)