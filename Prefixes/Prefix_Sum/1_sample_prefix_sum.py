# Input
arr = [3, 1, 5, 2]

 # Calculate prefix sum
psum = [0,0,0,0]

psum[0] = arr[0]

# Iterates and calculate prefix sum

for i in range(1,len(arr)):
    psum[i] = psum[i-1] + arr[i]


print(f"Original Array is {arr}")
print(f"psum is {psum}")