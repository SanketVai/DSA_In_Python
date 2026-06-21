# Build the prefix sum array manually.
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

# Using your prefix array, calculate: Sum(1,2)

sum = psum[2] - psum[1-1]

print(f"Sum of (1,2) is : {sum}")

# Q1 Sum(2,3)
print(f"Sum of (2,3) is {psum[3] - psum[1]}")


# Q2 Sum(0,2)
print(f"Sum of (0,2) {psum[2] - psum[0]}")