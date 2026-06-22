# def fixed_size_max_sum(arr,k):
#     if len(arr) == 0:
#         return 0
#     if len(arr) < k:
#         return 0
#     window_sum = sum(arr[:k])
#     max_sum = window_sum

#     for i in range(k,len(arr)):
#         print(f"Window Sum {window_sum}")
#         print(f"Max Sum {max_sum}")
#         window_sum = (window_sum - arr[i-k]) + arr[i]
#         max_sum = max(max_sum,window_sum)
    
#     return max_sum

# # Input
# arr = [2, 1, 5, 1, 3, 2]
# k = 3

# # output 9
# result = fixed_size_max_sum(arr,k)
# print(f"Max sum for Given window size is {result}")


def fixed_size_max_sum(arr, k):
    if len(arr) < k:
        return 0

    window_sum = sum(arr[:k])
    max_sum = window_sum

    print(f"Window {arr[:k]} -> Sum = {window_sum}")

    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)

        print(f"Window {arr[i-k+1:i+1]} -> Sum = {window_sum}")

    return max_sum


arr = [2, 1, 5, 1, 3, 2]
k = 3

result = fixed_size_max_sum(arr, k)
print("Max Sum =", result)