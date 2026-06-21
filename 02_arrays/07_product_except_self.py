def build_prefix_product(arr):
    if len(arr) == 0:
        return []
    prefix_product = [1] * len(arr)
    for i in range(1, len(arr)):
        prefix_product[i] = arr[i-1] * prefix_product[i-1]
    
    return prefix_product

def build_postfix_product(arr):
    if len(arr) == 0:
        return []
    postfix_product = [1] * len(arr)
    for i in range(len(arr)-2, -1, -1):
        postfix_product[i] = postfix_product[i+1] * arr[i+1]
    
    return postfix_product

def product_except_self(arr):
    if len(arr) == 0:
        return []
    prefix_product = build_prefix_product(arr)
    postfix_product = build_postfix_product(arr)
    answer = [1] * len(arr)
    for i in range(0,len(arr)):
        answer[i] = prefix_product[i] * postfix_product[i]
    
    return answer


# Input
arr = [2, 3, 4]
print(f"Product of given arr except self for {arr} is {product_except_self(arr)}")
#output [12, 8, 6]