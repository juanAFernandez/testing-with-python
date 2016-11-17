"""
Run:
    > nosetests -v nose_example.py
"""

def stupid_function(a, b):
    return a+b

def stupid_test():
    assert stupid_function(2,8) == 1
