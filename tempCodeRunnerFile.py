def binarySearch(array,x,low,high):

# 	while low <=high:

# 		mid =low +(high - low) //2

# 		if array[mid] == x:
# 			return mid

# 		elif array [mid] < x:
# 			low = mid+1

# 		else:
# 			high = mid -1

# 	return -1

# array =[3,4,5,6,7,8,9]
# x = 4

# result = binarySearch(array,x,0,len(array)-1)

# if result !=-1:
# 	print("Element is at index " +  str (result))
# else:
# 	print("Not found")


# def BinarySearch(list,element,low,high):

# 	while low <= high:

# 		mid = low +(high - low)//2

# 		if list[mid] == element:
# 			return mid

# 		elif list[mid] < element:
# 			low = mid +1
# 		else:
# 			high =mid -1

# 	return -1

# list =[2,4,5,6,7]

# element = 5  # Finding element

# result = BinarySearch(list,element,0,len(list)-1)

# if result !=-1:
# 	print("Finding the value " + str(result))
# else:
# 	print("not found")