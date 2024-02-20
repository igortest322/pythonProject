def search_element(array, element):
    if not array:
        return -1

    index = 0
    while index < len(array):
        if array[index] == element:
            return index

        index += 1

    return -1

if __name__ == "__main__":
    # Get the array from the user
    array_str = input("Enter the array elements: ")
    array = list(map(int, array_str.split()))

    # Get the element to search for from the user
    element = int(input("Enter the element to search for: "))

    index = search_element(array, element)
    if index != -1:
        print(element, "is found at index", index)
    else:
        print(element, "is not found in the array")





# def search_element(array, element):
#     if not array:
#         return -1

#     index = 0
#     while index < len(array):
#         if array[index] == element:
#             return index

#         index += 1

#     return -1

# if __name__ == "__main__":
#     array = [1, 2, 3, 4, 5]
#     element = 3

#     index = search_element(array, element)
#     if index != -1:
#         print(element, "is found at index", index)
#     else:
#         print(element, "is not found in the array")