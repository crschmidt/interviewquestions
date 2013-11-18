#!/usr/bin/python
"""
Module containing function with simple paren/brace matcher.
"""

import doctest
def matched(string):
    """
    >>> matched('()')
    True
    >>> matched('(]')
    False
    >>> matched('[{()}]')
    True
    >>> matched('[{()]}')
    False
    >>> matched('[{()}]]')
    False
    """
    match = {
        '{': '}',
        '[': ']',
        '(': ')'
    }
    state = []
    for char in string:
        if char in match.keys():
            state.append(char)
        elif char in match.values():
            if not len(state):
                return False
            last = state.pop()
            if match[last] != char:
                return False
    return len(state) == 0
if __name__ == "__main__":
    doctest.testmod()
