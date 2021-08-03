"""
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary
representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
"""


def count_bits(n):
    a = str("{0:b}".format(n))
    print(a.count("1"))


count_bits(1234)





# Explanation: covert the dec number to bin and covert this bin number to a string
# then count the number of 1s in the string using count method



'''
def countBits(n):
    return bin(n).count("1")
'''

'''
def countBits(n):
    return '{:b}'.format(n).count('1')
'''