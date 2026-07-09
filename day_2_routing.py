"""
Python If Statement: Syntax, Usage, and Examples

In Python, conditional statements like the if statement are control flow statements
that run (or skip) blocks of code based on specified conditions.

Quick Answer: How to Use if with and & or
A Python if statement executes a block of code if its condition is True.
You can combine multiple conditions using the logical operators 'and' and 'or'.
====================================
    and: All conditions must be True.
    or: At least one condition must be True.
    You can chain checks with elif (else if) and provide a default with else.
"""

age = 25
is_student = False

if age < 18:
    print("You are a minor.")
elif age >= 18 and is_student:
    print('You are a major and qualify for a student discount.')
else:
    print('You are an adult but not a student!')
# =====================================
"""
Python if statement executes a block of code if its condition is True.
How to use an if Statement in Python:
If statement executes a block of code if its condition is True.
It can be extended with elif (else if) for additional conditions and
else for a default case where no condition is provided.
Conditions can be combined using the logical operators and and or.
"""
age = 25
has_license = False

if age >= 18 and has_license:
    print('You are eligible to drive.')
elif age < 18:
    print('You are too young to drive!')
else:
    print('You must have a license to drive!')




