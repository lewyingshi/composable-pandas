from composable import pipeable
import pandas as pd
import re


@pipeable
def capitalize(col):
    """Convert strings in the Series/Index to be capitalized.
    
    Equivalent to :meth:`str.capitalize`.
    
    Returns
    -------
    Series or Index of object
    
    See Also
    --------
    str.lower : Converts all characters to lowercase.
    str.upper : Converts all characters to uppercase.
    str.title : Converts first character of each word to uppercase and
        remaining to lowercase.
    str.capitalize : Converts first character to uppercase and
        remaining to lowercase.
    str.swapcase : Converts uppercase to lowercase and lowercase to
        uppercase.
    str.casefold: Removes all case distinctions in the string.
    
    Examples
    --------
    >>> s = pd.Series(['lower', 'CAPITALS', 'this is a sentence', 'SwApCaSe'])
    >>> s
    0                 lower
    1              CAPITALS
    2    this is a sentence
    3              SwApCaSe
    dtype: object
    
    >>> s >> capitalize
    0                 Lower
    1              Capitals
    2    This is a sentence
    3              Swapcase
    dtype: object
    
    """
    return col.str.capitalize()

@pipeable
def islower(col):
    """Check whether all characters in each string are lowercase.
    
    This is equivalent to running the Python string method
    :meth:`str.islower` for each element of the Series/Index. If a string
    has zero characters, ``False`` is returned for that check.
    
    Returns
    -------
    Series or Index of bool
        Series or Index of boolean values with the same length as the original
        Series/Index.
    
    See Also
    --------
    str.isalpha : Check whether all characters are alphabetic.
    str.isnumeric : Check whether all characters are numeric.
    str.isalnum : Check whether all characters are alphanumeric.
    str.isdigit : Check whether all characters are digits.
    str.isdecimal : Check whether all characters are decimal.
    str.isspace : Check whether all characters are whitespace.
    str.islower : Check whether all characters are lowercase.
    str.isupper : Check whether all characters are uppercase.
    str.istitle : Check whether all characters are titlecase.
    
    Examples
    --------
    **Checks for Character Case**
    
    >>> s = pd.Series(['leopard', 'Golden Eagle', 'SNAKE', ''])
    
    >>> s >> islower
    0     True
    1    False
    2    False
    3    False
    dtype: bool
    """
    return col.str.islower()

@pipeable
def isnumeric(col):
    """Check whether all characters in each string are numeric.
    
    This is equivalent to running the Python string method
    :meth:`str.isnumeric` for each element of the Series/Index. If a string
    has zero characters, ``False`` is returned for that check.
    
    Returns
    -------
    Series or Index of bool
        Series or Index of boolean values with the same length as the original
        Series/Index.
    
    See Also
    --------
    str.isalpha : Check whether all characters are alphabetic.
    str.isnumeric : Check whether all characters are numeric.
    str.isalnum : Check whether all characters are alphanumeric.
    str.isdigit : Check whether all characters are digits.
    str.isdecimal : Check whether all characters are decimal.
    str.isspace : Check whether all characters are whitespace.
    str.islower : Check whether all characters are lowercase.
    str.isupper : Check whether all characters are uppercase.
    str.istitle : Check whether all characters are titlecase.
    
    Examples
    --------
    >>> s = pd.Series(['23', '³', '⅕', ''])

        The ``s.str.isnumeric`` method is the same as ``s.str.isdigit`` but also
    includes other characters that can represent quantities such as unicode
    fractions.
    
    >>> s >> isnumeric
    0     True
    1     True
    2     True
    3    False
    dtype: bool
    """
    return col.str.isnumeric()

@pipeable
def istitle(col):
    """Check whether all characters in each string are titlecase.
    
    This is equivalent to running the Python string method
    :meth:`str.istitle` for each element of the Series/Index. If a string
    has zero characters, ``False`` is returned for that check.
    
    Returns
    -------
    Series or Index of bool
        Series or Index of boolean values with the same length as the original
        Series/Index.
    
    See Also
    --------
    str.isalpha : Check whether all characters are alphabetic.
    str.isnumeric : Check whether all characters are numeric.
    str.isalnum : Check whether all characters are alphanumeric.
    str.isdigit : Check whether all characters are digits.
    str.isdecimal : Check whether all characters are decimal.
    str.isspace : Check whether all characters are whitespace.
    str.islower : Check whether all characters are lowercase.
    str.isupper : Check whether all characters are uppercase.
    str.istitle : Check whether all characters are titlecase.
    
    Examples
    --------
    **Checks for Character Case**

    >>> s = pd.Series(['leopard', 'Golden Eagle', 'SNAKE', ''])

    The ``s.str.istitle`` method checks for whether all words are in title
    case (whether only the first letter of each word is capitalized). Words are
    assumed to be as any sequence of non-numeric characters separated by
    whitespace characters.
    
    >>> s >> istitle
    0    False
    1     True
    2    False
    3    False
    dtype: bool
    """
    return col.str.istitle()

@pipeable
def isupper(col):
    """Check whether all characters in each string are uppercase.
    
    This is equivalent to running the Python string method
    :meth:`str.isupper` for each element of the Series/Index. If a string
    has zero characters, ``False`` is returned for that check.
    
    Returns
    -------
    Series or Index of bool
        Series or Index of boolean values with the same length as the original
        Series/Index.
    
    See Also
    --------
    str.isalpha : Check whether all characters are alphabetic.
    str.isnumeric : Check whether all characters are numeric.
    str.isalnum : Check whether all characters are alphanumeric.
    str.isdigit : Check whether all characters are digits.
    str.isdecimal : Check whether all characters are decimal.
    str.isspace : Check whether all characters are whitespace.
    str.islower : Check whether all characters are lowercase.
    str.isupper : Check whether all characters are uppercase.
    str.istitle : Check whether all characters are titlecase.
    
    Examples
    --------
    **Checks for Character Case**
    
    >>> s = pd.Series(['leopard', 'Golden Eagle', 'SNAKE', ''])

    >>> s >> isupper
    0    False
    1    False
    2     True
    3    False
    dtype: bool
    """
    return col.str.isupper()

@pipeable
def isspace(col):
    """Check whether all characters in each string are alphanumeric.
    
    This is equivalent to running the Python string method
    :meth:`str.isalnum` for each element of the Series/Index. If a string
    has zero characters, ``False`` is returned for that check.
    
    Returns
    -------
    Series or Index of bool
        Series or Index of boolean values with the same length as the original
        Series/Index.
    
    See Also
    --------
    str.isalpha : Check whether all characters are alphabetic.
    str.isnumeric : Check whether all characters are numeric.
    str.isalnum : Check whether all characters are alphanumeric.
    str.isdigit : Check whether all characters are digits.
    str.isdecimal : Check whether all characters are decimal.
    str.isspace : Check whether all characters are whitespace.
    str.islower : Check whether all characters are lowercase.
    str.isupper : Check whether all characters are uppercase.
    str.istitle : Check whether all characters are titlecase.
    
    Examples
    --------
    **Checks for Whitespace**

    >>> s = pd.Series([' ', '\\t\\r\\n ', ''])
    >>> s >> isspace
    0     True
    1     True
    2    False
    dtype: bool
    """
    return col.str.isspace()