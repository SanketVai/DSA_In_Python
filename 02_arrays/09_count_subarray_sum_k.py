def count_subarray_sum_k(arr,k):
    if len(arr) == 0:
        return 0
    prefix = 0
    count = 0
    freq = {0:1}
    for num in arr:
        prefix += num
        if prefix - k in freq:
            count += freq[prefix-k]
        freq[prefix] = freq.get(prefix,0) + 1
    return count


# Input
arr = [1, 1, 1, 1]
k = 2

print(f"Total Subarray count for given input{arr} for {k} = {count_subarray_sum_k(arr,k)}")
