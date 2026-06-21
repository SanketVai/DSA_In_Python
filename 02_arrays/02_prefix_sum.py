def build_prefix_sum(arr):
    if len(arr) == 0:
        return []
    prefix_sum = len(arr) * [0]
    prefix_sum[0] = arr[0]
    for i in range(1, len(arr)):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]
    return prefix_sum


def range_sum(prefix,left,right):
    if len(prefix) == 0: 
        return 0
    if left == 0:
        return prefix[right]
    total_sum = prefix[right] - (prefix[left-1] )
    return total_sum


arr = [4, 2, 7, 1, 3]
prefix = build_prefix_sum(arr)
print(f"Prefix Sum of Given Array {arr} is {prefix}")
print(f"Range Sum 0 and 2 for prefix {prefix} is {range_sum(prefix,0,2)}")
print(f"Range Sum of 2 and 4 for prefix {prefix} is {range_sum(prefix,2,4)}")
