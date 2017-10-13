"""
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
For problems such as these, do not include raw_input statements or define 
the variable s in any way. Our automating testing will provide a value of 
s for you - so the code you submit in the following box should assume s is 
already defined.
"""

count = 0
word = "bob"
for i in range(len(s)-(len(word)-1)):
    if s[i:i+len(word)] == word:
        count += 1
print("Number of times",word,"occurs is:",count)
