def min_sum_subarray(arr,k):
    if len(arr) == 0 or len(arr) < k: 
        return 0
    window_sum = sum(arr[:k])
    min_sum = window_sum

    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        min_sum = min(window_sum,min_sum)
    
    return min_sum 


arr = [2, 1, 5, 1, 3, 2]
k = 3

print(f"Min sum for given array is {min_sum_subarray(arr,k)}")
