def build_postfix_product(arr):
    if len(arr) == 0:
        return []
    
    postfix_product = [0] * len(arr)
    postfix_product[len(arr) - 1] = 1

    for i in range(len(arr) - 2, -1, -1):
        postfix_product[i] = arr[i+1] * postfix_product[i+1]
    
    return postfix_product




# Input
arr = [2, 3, 4]
print(f"Postfix product of given {arr} is {build_postfix_product(arr)}")

