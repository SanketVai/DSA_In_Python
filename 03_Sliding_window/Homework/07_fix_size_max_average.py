def build_max_avg_subarray(arr,k):
    if len(arr) == 0:
        return 0
    
    sum_subarray = sum(arr[:k])
    max_avg = sum_subarray

    for i in range(k,len(arr)):
        sum_subarray = sum_subarray - arr[i-k] + arr[i]
        max_avg = max(sum_subarray,max_avg)
    
    return max_avg/k


arr = [1, 12, -5, -6, 50, 3]
k = 4


print(f"max sum avg for given {arr} for {k} size is {build_max_avg_subarray(arr,k)}")