"""
Alphabetical Substrings
Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters 
occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your 
program should print:
Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', 
then your program should print:
Longest substring in alphabetical order is: abc
For problems such as these, do not include raw_input statements or define the 
variable s in any way. Our automating testing will provide a value of s for 
you - so the code you submit in the following box should assume s is already 
defined. 
"""

sub = s[0]
var = s[0]
for i in range(len(s)-1):
    if s[i+1] >= s[i]:
        var += s[i+1]
        if len(var) > len(sub):
            sub = var
    else:
        var = s[1+i]
print("Longest substring in alphabetical order is:", sub)
