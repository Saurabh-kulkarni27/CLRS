import unittest

#when 2 strings have same length
def check_same_length(s1,s2):
    edit = False

    for i,j in zip(s1,s2):
        #print(i,j)
        if i != j:
            if edit:
                #for 2nd difference in string return false
                return(False)
            else:
                #1st difference
                edit = True
    #print('True')
    return(True)

#for strings of different size
def check_diff_length(s1, s2):
    i,j = 0,0
    edit = 0
    
    #
    while(i<len(s1) and j<len(s2)):
        if s1[i] != s2[j]:
            i += 1
            edit += 1

        else:
            i += 1
            j += 1

    if edit > 1:
        return False
    else:
        return True





def check_one_edit(s1,s2):
    #print(str1,str2)


    m = len(s1)
    n = len(s2)

    #if strings length is difference is greater than 1, return false directly
    if (abs(m-n) > 1):
        return False

    #3 cases possible
    #1: both strings have same length
    if m == n:
        result=check_same_length(s1,s2)
        return (result)
        
    #1st string length is more
    elif m > n:
        result = check_diff_length(s1, s2)
        return (result)
    
    #2nd string length is more
    else:
        result = check_diff_length(s2, s1)
        return (result)


class Test(unittest.TestCase):
    #print('1')
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = check_one_edit(test_s1, test_s2)
            #print(test_s1,test_s2,actual,expected)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
    
#unitest cases reference: https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/Chapter1/5_One%20Away/OneAway.py
