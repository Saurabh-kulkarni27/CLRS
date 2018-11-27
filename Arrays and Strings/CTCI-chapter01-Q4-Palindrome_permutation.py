'''
Problem Statement: Given a string, w.a.f. to check if it is a permutation of a palindrome.

Input: 'taco cat'
Output: True.  [permutation: 'taco cat', 'atco cta']


Approach: using dictionary data structure
'''

#---------


def is_permutation(input_string):
    print(input_string)
    dic = {}
    for letter in input_string.replace(' ', ''):
        if letter not in dic:
            dic[letter] = 1
        else:
            dic[letter] += 1

    print(dic)
    check = dic.values()
    count = 0
    for x in check:
        if x == 1:
            count += 1
    return False if count > 1 else True


#---------

def main():
    input_string = 'Not a Palindrome'

    result = is_permutation(input_string.lower())

    print(result)


main()
