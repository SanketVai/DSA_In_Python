def max_avg_subarray(arr,k):
    if len(arr) == 0 or len(arr) < k:
        return 0
    window_sum = sum(arr[:k])
    max_avg = 0 / k
    for i in range(k,len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_avg = max(window_sum/k,max_avg)
    
    return max_avg





arr = [1, 12, -5, -6, 50, 3]
k = 4

print(f"Maximum Avg for given {arr} is {max_avg_subarray(arr,k)}")



# Since k is fixed, you can just track the maximum sum and divide once at the end:


def max_avg_subarray(arr, k):
    if len(arr) < k:
        return 0

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum / k
