from unittest import *    
import doctest
import io
from contextlib import redirect_stdout


def my_function():  
    """Doctest
    >>> my_function()
    Hello World\n
    """
    print("Hello World")

doctest.testmod()


def function_to_doctest(a):
    """
    Deze functie neemt een reeks van getallen en sorteert deze in oplopende volgorde.
    @param a de lijst om te sorteren
    @return de gesorteerde variant van a
    >>> function_to_doctest([1,3,2])
    [1, 2, 3]
    """
    a.sort()
    return a


doctest.testmod()