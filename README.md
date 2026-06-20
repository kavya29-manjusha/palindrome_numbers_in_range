# 🔁 Palindrome Numbers in a Given Range

## 📌 Project Overview

This Python project finds all palindrome numbers within a given range. A palindrome number is a number that remains the same when its digits are reversed.

Example:
121 → 121 ✔️ (Palindrome)
123 → 321 ❌ (Not a Palindrome)

---

## 🚀 Features

* Takes a range of numbers
* Checks each number for palindrome property
* Displays all palindrome numbers in that range
* Simple and beginner-friendly Python logic

---

## 🧠 Logic Used

1. Take each number in the given range
2. Reverse the number using a loop
3. Compare reversed number with original number
4. If both are equal → print the number

---

## 💻 Code

```python
# Function to check palindrome
def isPalindrome(n):
    reverse = 0
    temp = n

    while temp > 0:
        reverse = reverse * 10 + temp % 10
        temp = temp // 10

    return n == reverse

# Range values
min_val = 100
max_val = 150

# Find palindrome numbers in range
for i in range(min_val, max_val + 1):
    if isPalindrome(i):
        print(i, end=" ")
```

---

## 📊 Example Output

```
101 111 121 131 141
```

---

## 🎯 Learning Outcomes

* Understanding loops in Python
* Number manipulation techniques
* Conditional statements
* Basic algorithmic thinking

---

## 👩‍💻 Author

Kavya Manjusha
Passionate about Python, AI, and Software Development 🚀
