def quickSort(list):
	if len(list) < 2:
		return list
	else:
		pivot = list[0]
		less = [i for i in list[1:] if i < pivot]
		great = [i  for i in list[1:] if i> pivot]
		return quickSort(less) + [pivot] + quickSort(great)

print(quickSort([9, 7, 8, 5, 3, 0, 1]))