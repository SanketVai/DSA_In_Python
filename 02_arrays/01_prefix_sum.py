def build_prefix_sum(arr):
    if len(arr) == 0:
        return []
    prefix_sum = len(arr) * [0]
    prefix_sum[0] = arr[0]
    for i in range(1, len(arr)):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]
    return prefix_sum

arr = [4, 2, 7, 1, 3]
prefix = build_prefix_sum(arr)
print(f"Prefix Sum of Given Array {arr} is {prefix}")

