#!/usr/bin/env python

def varNumArguments(*args, **kwargs):
    """
    A function to test *args and **kwargs.

    *args denotes variable number of positional arguments.
    **kwargs denotes variable number of keyword arguments.
    **kwargs must come after *args.
    """

    # *args are stored in a tuple named args
    print(type(args), args, sep=' ')
    # **kwargs are stored in a dict named kwargs
    print(type(kwargs), kwargs, sep=' ')
    
    sumKA = 0
    
    for kwarg in kwargs:
        sumKA += kwargs[kwarg]
        
    print(sum(args), sumKA, sep='\n')

if __name__ == '__main__':
    
    varNumArguments(11, 26, 3000, 43, five=5, six=6, seven=7, eight=8)
    
    # datatypes dict, list, set and tuple, are built-in python container datatypes
    # they can be unpacked with * (list, set, tuple) or ** (dict)
    
    aList = [100, 99, 98, 97, 96]
    aSet = set([7, 8, 9, 10])
    aTuple = ('one', 'two', 'three')
    aDict = {'fifteen': 15, 'thirty': 30, 'fortyfive': 45}
    
    a, *b, c = aList
    d, e, *f = aSet
    *g, h = aTuple
    
    print(a, b, c, sep=' ')
    print(d, e, f, sep=' ')
    print(g, h, sep=' ')
    
    varNumArguments(**aDict)