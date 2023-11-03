for num in range(26):
    alpha = chr(ord("a") + num)
    print(alpha)

import string
 
for letter in string.ascii_lowercase:
    print(letter)
# Explanation: 

# string  is a built-in module and string.ascii_lowercase  returns a string object containing all 26 letters of the English alphabet. Then we simply iterate through that string and print out the string items.