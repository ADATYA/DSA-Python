def binary_search(array, target):
  """
  Performs a binary search on the given array for the target value.

  Args:
    array: The array to search.
    target: The value to search for.

  Returns:
    The index of the target value in the array, if found.
    -1 if the target value is not found.
  """

  # Check if the array is empty.
  if len(array) == 0:
    return -1

  # Initialize the low and high indexes.
  low = 0
  high = len(array) - 1

  # Loop while the low index is less than or equal to the high index.
  while low <= high:
    # Calculate the middle index.
    mid = (low + high) // 2

    # Compare the target element to the element at the middle index.
    if array[mid] == target:
      # The target element is found.
      return mid
    elif array[mid] < target:
      # The target element is greater than the element at the middle index.
      low = mid + 1
    else:
      # The target element is smaller than the element at the middle index.
      high = mid - 1

  # The target element is not found.
  return -1


def bubble_sort(array):
  """
  Performs a bubble sort on the given array.

  Args:
    array: The array to sort.

  Returns:
    The sorted array.
  """

  # Loop through the array, comparing adjacent elements.
  for i in range(len(array) - 1):
    for j in range(len(array) - i - 1):
      # If the current element is greater than the next element, swap them.
      if array[j] > array[j + 1]:
        array[j], array[j + 1] = array[j + 1], array[j]

  return array
