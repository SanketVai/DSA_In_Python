def max_even_number_subarray(arr,k):
    if len(arr) == 0 or len(arr) < k:
        return 0
    
    window_even_count  = sum(1 for x in arr[:k] if x % 2 == 0)
    max_even = window_even_count
    for i in range(k,len(arr)):
        if arr[i-k] % 2 == 0:
            window_even_count -= 1
        if arr[i] % 2 == 0:
            window_even_count += 1
        max_even = max (max_even,window_even_count)
    
    return max_even



# Input
arr = [2, 1, 8, 3, 6, 4, 7, 10]
k = 3

print(f"Max Even number for given array is {max_even_number_subarray(arr,k)}")
