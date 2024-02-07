# def find_min(nums):
#     if not nums:
#         raise ValueError("Invalid input: nums must be a non-empty list")

#     min_value = nums[0]
#     for num in nums[1:]:
#         if num < min_value:
#             min_value = num

#     return min_value

# if __name__ == "__main__":
#     nums = [1, 5, 2, 4, 3]
#     min = find_min(nums)
#     print("The minimum value in the array", nums, "is", min)

def find_min(nums):
    if not nums:
        raise ValueError("Invalid input: nums must be a non-empty list")

    min_value = nums[0]
    for num in nums[1:]:
        if num < min_value:
            min_value = num

    return min_value

if __name__ == "__main__":
    nums = list(map(int, input("Enter the array of numbers: ").split()))
    min = find_min(nums)
    print("The maximum value in the array", nums, "is", min)