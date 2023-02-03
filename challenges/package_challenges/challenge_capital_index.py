"""
Capital indexes
Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.
For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
"""
import re
def capital_indexes(test_string):
    return ([i for i, j in enumerate(test_string) if re.match('[A-Z]',j)])

final = capital_indexes("ManoM")
print (final)
