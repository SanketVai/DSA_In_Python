def build_prefix_max(arr):
    if len(arr) == 0:
        return []
    prefix_max = [0] * len(arr)
    prefix_max[0] = arr[0]
    for i in range(1,len(arr)):
        prefix_max[i] = max(arr[i], prefix_max[i-1])
    return prefix_max





arr = [5, 1, 8, 2, 6]
print(f"Prefix Max for given input {arr} is {build_prefix_max(arr)}")
# prefix_max[3] stores the maximum value from index 0 to index 3 (inclusive).