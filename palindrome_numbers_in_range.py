# 02:Find all Palindrome Numbers in a given range 
# Problem Statement: Given a range of numbers, find all the palindrome numbers in the range.
# A function to check if n is palindrome
def isPalindrome(n):
    reverse = 0
    temp = n
    # Reverse the number
    while temp > 0:
        reverse = reverse * 10 + temp % 10
        temp = temp // 10
    return n == reverse
min_val = 100
max_val = 150
for i in range(min_val, max_val + 1):
    if isPalindrome(i):
        print(i, end=" ")