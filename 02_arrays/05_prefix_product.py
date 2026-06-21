def build_prefix_product(arr):
    if len(arr) == 0:
        return []
    prefix_product = [0] * len(arr)
    prefix_product[0] = 1
    for i in range(1, len(arr)):
        prefix_product[i] = arr[i-1] * prefix_product[i-1]

    return prefix_product


# Input
arr = [2, 3, 4]

print(f"Prefix Product for given array {arr} is {build_prefix_product(arr)}")
# Expected Output
# [1, 2, 6]