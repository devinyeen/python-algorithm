# Sum with recursive

def sum(list):
	if list == []:
		return 0;
	return list[0]+sum(list[1:])

print(sum([1,2,3,4]))


def count(list):
	if list == []:
		return 0
	return 1 + len(list[1:])
print(count([1,2,3,4]))

#def biggest(list):
#	if list