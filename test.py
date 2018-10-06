#squares = [value**2 for value in range(1,11)]
#print(squares)

#for value in range(1,6):
#	print(value**2)

def findSmallest(arr):
	smallest = arr[0]
	smallestIndex = 0
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallestIndex = i
	return smallestIndex

def selectionSort(arr):
	newArr = []
	for i in range(len(arr)):
		smallest = findSmallest(arr)
		newArr.append(arr.pop(smallest))
	return newArr

my_list = [1, 3, 5, 7, 9]
print(selectionSort([5,3,6,2,10]))