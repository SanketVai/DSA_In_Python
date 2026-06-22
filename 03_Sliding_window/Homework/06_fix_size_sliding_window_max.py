from collections import deque

def sliding_window_maximum(arr,k):
    if len(arr) == 0:
        return []
    
    dq = deque()
    answer = []

    for right in range(len(arr)):
        left = right - k + 1

        # Remove the out of window index
        if dq and dq[0]  < left:
            dq.popleft()
        
        # Remove the index from last
        while dq and arr[dq[-1]] < arr[right]:
            dq.pop()
        

        # add index of incoming value
        dq.append(right)

        # Close the window and put the max in answer list
        if right >= k - 1:
            answer.append(arr[dq[0]])
            print(answer)
            print(dq)

    return answer
# Input
arr = [2,1,5,3,7,2,6]
k = 3

# Output
result = sliding_window_maximum(arr,k)
print(f"Maximum values for subarray size of {k} is {result}")