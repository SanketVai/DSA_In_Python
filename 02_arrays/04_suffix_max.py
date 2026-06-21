def build_suffix_max(arr):
    if len(arr) == 0:
        return []
    
    suffix_max = [0] * len(arr)
    suffix_max[len(arr) - 1] = arr[len(arr)-1]

    for i in range(len(arr)-2,-1,-1):
        suffix_max[i] = max(arr[i], suffix_max[i+1])

    return suffix_max 


arr = [5, 1, 8, 2, 6]
print(f"Suffix Max for given array is {arr} is {build_suffix_max(arr)}")

#suffix_max[2] stores the maximum value from index 2 to the last index (n-1).