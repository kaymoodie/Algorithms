    1 	# Selection Sort
    2 	
    3 	# List of unsorted numbers
    4 	list_of_num = [45, 27, 13, 98, 16, 104 ,20, 67, 73, 34 ]
    5 	
    6 	# Display list of unsorted numbers
    7 	print("Unsorted")
    8 	for item in list_of_num:
    9 	    print(item)
   10 	
   11 	# Get the how many numbers there is in the list
   12 	length = len(list_of_num)
   13 	# The number of sorted items
   14 	number_of_sorted_items = 0
   15 	# Initialize index values
   16 	# The index to start sorting from
   17 	index = 0
   18 	# The index of the smallest value
   19 	min_index = 0
   20 	
   21 	# Run once the number  of unsorted items is less than the number of items in the initial list
   22 	while number_of_sorted_items < length - 1:
   23 	    # Set the smallest current value to the value store at the current index
   24 	    current_minimun = list_of_num[index]
   25 	    
   26 	    # Go through the list of numbers
   27 	    for next_index in range(index, length):
   28 	        # Check if the number at the next index is less than the current smallest value
   29 	        if list_of_num[next_index] < current_minimun:
   30 	            # If true
   31 	            # Set the smallest value to the value at the current index
   32 	            current_minimun = list_of_num[next_index]
   33 	            # Set the smallest index the the current index
   34 	            min_index = next_index
   35 	
   36 	    # After all the values are checked from the initial index
   37 	    # Create a temporary value for the value stored at the initial index
   38 	    temp = list_of_num[index]
   39 	    # Set the value at the initial index to the smallest value determined 
   40 	    list_of_num[index] = current_minimun
   41 	    # Set the value of the index where the smallest value was initially store to the value of the initial index
   42 	    list_of_num[min_index] = temp
   43 	    # Increase the initial index i.e. what index to start sorting from
   44 	    index += 1
   45 	    # Increase the number of items stored to 1
   46 	    number_of_sorted_items += 1
   47 	
   48 	# Display the sorted list
   49 	print("\nSorted")
   50 	for item in list_of_num:
   51 	    print(item)
