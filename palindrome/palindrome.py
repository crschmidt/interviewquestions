import math

def palindrome(s):
    """
    >>> palindrome("abc")
    False
    >>> palindrome("aba")
    True
    >>> palindrome("racecar")
    True
    >>> palindrome("aa")
    True
    """
    ret = True
    for i in range(int(math.ceil(float(len(s))/2))):
        if s[i] != s[-(1+i)]:
            ret = False
            break
    return ret
    

def palindrome2(s):
    """
    >>> palindromde2(" a b  a")
    True
    >>> palindrome2("a  a")
    True
    >>> palindrome2("acb  ca")
    True
    >>> palindrome2("acb")
    False
    """
    ret = True
    neg = -1
    for i, char in enumerate(s):
        if char == " ":
            continue
        while s[neg] == " ":
            neg -= 1
        if s[neg] != char:
            ret = False
            break
        neg -= 1 
        if i + abs(neg) > len(s):
            break     
    return ret

