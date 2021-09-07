# The goal of this exercise is to convert a string to a new string where each character in the new
# string is "(" if that character appears only once in the original string, or ")" if that character appears
# more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
#
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("



def duplicate_encode(word):
    count = {}
    new_word = ""
    word = word.lower()
    for ch in word:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
    for k in word:
        if count[k] > 1:
            new_word += ')'
        else:
            new_word += '('
    print(new_word)


duplicate_encode("abca)")



# def duplicate_encode(word):
#     return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])


# from collections import Counter
#
# def duplicate_encode(word):
#     word = word.lower()
#     counter = Counter(word)
#     return ''.join(('(' if counter[c] == 1 else ')') for c in word)


# def duplicate_encode(word):
#     new_string = ""
#     word = word.lower()
#
#     for char in word:
#         new_string += (")" if (word.count(char) > 1) else "(")
#
#     return new_string