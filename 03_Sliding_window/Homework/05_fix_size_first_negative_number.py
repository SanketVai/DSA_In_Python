from collections import deque

def first_negative_number_in_subarray(arr,k):
    if len(arr) < k:
        return []
   
    result = []
    negatives = deque()

    for i in range(len(arr)):

        # Add current negative number
        if arr[i] < 0: 
            negatives.append(i)
        
        # Remove indices out of window
        while negatives and negatives[0] <= i-k:
            negatives.popleft()
        
        # Window Formed
        if i >= k-1:
            if negatives:
                result.append(arr[negatives[0]])
            else:
                result.append(0)
    return result

# Input
arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3

# output
result = first_negative_number_in_subarray(arr,k)
print(f"List of first negative number for subarray of size {k} is {result}")

