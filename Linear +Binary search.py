def linear_search(number_list,number_of_find):
    for index , element in enumerate(number_list):
        if element == number_of_find:
              return index
    return -1



def binary_search (number_list,number_of_find):
    left_index = 0
    right_index = len(number_list) -1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) //2
        mid_number = number_list[mid_index]

        if mid_index == number_of_find:
            return mid_index

        if mid_index <number_of_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index -1

    return -1

if __name__ == '__main__':
    number_list = [12,34,67,78,43,21]
    number_of_find = 21

    index = linear_search(number_list,number_of_find)
    print(f"Number is found at index [{ index }] using linear search")
