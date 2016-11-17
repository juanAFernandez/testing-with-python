def sum(a, b):
    """
    >>> sum(2, 4)
    6
    >>> sum('a', 'b')
    'ab'
    """
    return a+b+b


print sum(3,4)
print sum('Hi', 'bye')


if __name__ == "__main__":
    import doctest
    doctest.testmod()