def length_of_longest_substring(s):
    start = 0
    max_len = 0
    seen = {}
    for i, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        seen[char] = i
        max_len = max(max_len, i - start + 1)
    return max_len

# User Input
s = input("Enter a string: ")
print("Length of longest substring without repeating characters:", length_of_longest_substring(s))
