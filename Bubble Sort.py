#Bubble Sort

num_list = [90, 43, 55, 23, 98, 45, 76, 88, 59, 36, 47]


print("Unsorted List")
for num in num_list:
    print(num)
    
length = len(num_list)
counter = length
index_1 = 0
index_2 = 1
last_index = length - 1
# i = 1 # Debugging assistant
sorted_index = 0

while counter > 0:
    # print(f"\nCheck # {i}") # Debugging assistant
    if num_list[index_2] < num_list[index_1]:
        # print(f"{num_list[index_2]} is smaller than {num_list[index_1]}!") # Debugging assistant
        temp = num_list[index_1]
        num_list[index_1] = num_list[index_2]
        num_list[index_2] = temp
      
    
    index_1 = index_2
    index_2 += 1      
    # i += 1 # Debugging assistant

    if index_2 == length:
        counter -= 1
        index_1 = 0
        index_2 = 1
       
print("\nSorted List")
for num in num_list:
    print(num)

    

# Python program for implementation of Bubble Sort

def bubbleSort(arr):
	n = len(arr)

	# Traverse through all array elements
	for i in range(n-1):
	# range(n) also work but outer loop will repeat one time more than needed.

		# Last i elements are already in place
		for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j + 1] :
				arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

print ("Unsorted array is:")
for i in range(len(arr)):
	print ("% d" % arr[i]),


bubbleSort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
	print ("% d" % arr[i]),
