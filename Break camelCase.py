"""
Complete the solution so that the function will break up camel casing, using a space between words.
Example

"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""

"""


import re

def solution(s):
    print(re.sub(r'(\B)([A-Z])(\B)', r'\1 \2', s))


solution('breakCamelcase')
solution('helloWorld')
solution('camelCase')







'''
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)
'''


'''
import re
def solution(s):
    return re.sub('([A-Z])', r' \1', s)
'''