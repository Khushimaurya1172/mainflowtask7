def longest_palindrome(s):
    def expand_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    longest = ""
    for i in range(len(s)):
        odd = expand_center(i, i)
        even = expand_center(i, i+1)
        longest = max(longest, odd, even, key=len)
    return longest

# User Input
s = input("Enter a string: ")
print("Longest Palindromic Substring:", longest_palindrome(s))
