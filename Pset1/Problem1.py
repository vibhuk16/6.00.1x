"""
Counting Vowels
Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
For example, if s = 'azcbobobegghakl', your program should print:
Number of vowels: 5 
For problems such as these, do not include raw_input statements 
or define the variable s in any way. Our automating testing will provide 
a value of s for you - so the code you submit in the following box should 
assume s is already defined.
"""

count = 0
for letter in s:
    if letter in 'aeiou':
        count += 1
print("Number of vowels:", count)
