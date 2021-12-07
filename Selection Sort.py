# Selection Sort

list_of_num = [45, 27, 13, 98, 16, 104 ,20, 67, 73, 34 ]

print("Unsorted")
for item in list_of_num:
    print(item)
    
length = len(list_of_num)
number_of_sorted_items = 0
index = 0
min_index = 0

while number_of_sorted_items < length - 1:
    current_minimun = list_of_num[index]
    
    for next_index in range(index, length):
        if list_of_num[next_index] < current_minimun:
            current_minimun = list_of_num[next_index]
            min_index = next_index

    temp = list_of_num[index]
    list_of_num[index] = current_minimun
    list_of_num[min_index] = temp
    index += 1
    number_of_sorted_items += 1
    
print("\nSorted")
for item in list_of_num:
    print(item)