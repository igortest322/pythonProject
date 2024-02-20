def find_max(nums):
    if not nums:
        raise ValueError("Invalid input: nums must be a non-empty list")

    max_value = nums[0]
    for num in nums[1:]:
        if num > max_value:
            max_value = num

    return max_value

if __name__ == "__main__":
    nums = list(map(int, input("Enter the array of numbers: ").split()))
    maximum = find_max(nums)
    print("The maximum value in the array", nums, "is", maximum)






# def find_max(nums):
#     if not nums:
#         raise ValueError("Invalid input: nums must be a non-empty list")

#     max_value = nums[0]
#     for num in nums[1:]:
#         if num > max_value:
#             max_value = num

#     return max_value

# if __name__ == "__main__":
#     nums = [1, 5, 2, 4, 3]
#     maximum = find_max(nums)
#     print("The maximum value in the array", nums, "is", maximum)