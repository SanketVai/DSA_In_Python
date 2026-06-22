def build_max_vowels_count_in_subarray(input_string,k):
    if len(input_string) == 0 or len(input_string) < k:
        return 0
    vowel_list = {"a", "e", "i", "o", "u"}
    window_vowel_count = sum([1 for char in input_string[:k] if char in vowel_list])
    max_vowel = window_vowel_count
    for i in range(k,len(input_string)):
        if input_string[i-k] in vowel_list:
            window_vowel_count -= 1
        if input_string[i] in vowel_list:
            window_vowel_count += 1
        max_vowel = max (max_vowel,window_vowel_count)
    
    return max_vowel


# Input
s = "abciiidef"
k = 3

# Output
print(f"max number of vowels for given array for fix subarray is {build_max_vowels_count_in_subarray(s,k)}")