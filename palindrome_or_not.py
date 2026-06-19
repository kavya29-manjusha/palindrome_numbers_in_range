#01:This program checks whether a number is a palindrome or not.
def palindrome(n):
    revNum = 0
    dup = n
    while n > 0:
        ld = n % 10
        revNum = (revNum * 10) + ld
        n //= 10
        return dup == revNum
number = 4554 
if palindrome(number):  
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")