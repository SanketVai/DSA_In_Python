def subarray_sum_exists(arr,k):
    prefix = 0
    if len(arr) == 0:
        return False
    seen = {0}
    for i in range(0,len(arr)):
        prefix+= arr[i]
        if (prefix - k) in seen:
            return True
        else:
            seen.add(prefix)
    return False
    

#Input
arr = [1, 2, 1, 3]
k = 4

print(f"For given input {arr}, Subarray exists for value {k} = {subarray_sum_exists(arr,k)}")
# Output // True