
elem_count = input()
elem_count = int(elem_count)

arr_elems = input()

elem_list = arr_elems.split(' ')
elem_list = [int(items) for items in elem_list]

elem_sum = sum(elem_list)

output = int(elem_sum / elem_count)

print(output+1)