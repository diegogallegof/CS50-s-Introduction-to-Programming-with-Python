
# List comprehension

# Python List comprehension provides a much more short syntax 
# for creating a new list based on the values of an existing list.

#Advantages of List Comprehension
"""
 - More time-efficient and space-efficient than loops.
 - Require fewer lines of code.
 - Transforms iterative statement into a formula.
 """
# Syntax of  List Comprehension
"""
newList = [ expression(element) for element in oldList if condition ] 
"""
# ----------------------------------------------------------------
# Using list comprehension to iterate through loop
# ----------------------------------------------------------------
List = [character*2 for character in [1, 2, 3]]
# Displaying list
print(List)

# ----------------------------------------------------------------
# Example 2: Even list using list comprehension
# ----------------------------------------------------------------

