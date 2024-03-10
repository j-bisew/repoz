def partition(A,p,r):
  x=A[r]
  i=p-1
  for j in range (p, r+1):
    if A[j]<=x :
       i=i+1
       A[i], A[j] = A[j], A[i]
  if i<r :
     return i
  else:
    return i-1
  
def quickSort(A,p,r):
    if p<r :
        q = partition(A,p,r)
        quickSort(A,p,q)
        quickSort(A,q+1,r)
    return A


# def partition(array, low, high):
# 	pivot = array[high] #element najbardziej po prawej
     
# 	# pointer for greater element
# 	i = low - 1

# 	# porównujemy kazdy element z pivotem
# 	for j in range(low, high):
# 		if array[j] <= pivot: # If element smaller than pivot is found
# 			# swap it with the greater element pointed by i
# 			i = i + 1

# 			# Swapping element at i with element at j
# 			(array[i], array[j]) = (array[j], array[i])

# 	# Swap the pivot element with the greater element specified by i
# 	(array[i + 1], array[high]) = (array[high], array[i + 1])

# 	# Return the position from where partition is done
# 	return i + 1

# # function to perform quicksort


# def quickSort(array, low, high):
# 	if low < high:

# 		# Find pivot element such that
# 		# element smaller than pivot are on the left
# 		# element greater than pivot are on the right
# 		pi = partition(array, low, high)

# 		# Recursive call on the left of pivot
# 		quickSort(array, low, pi - 1)

# 		# Recursive call on the right of pivot
# 		quickSort(array, pi + 1, high)


data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(quickSort(data, 0, size - 1))
