from composable import pipeable
import pandas as pd


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
def is_month_start(col):
    """
    Return True if date is first day of month.
    """
    return col.dt.is_month_start

@pipeable
def is_quarter_start(col):
    """
    Return True if date is first day of the quarter.
    """
    return col.dt.is_quarter_start

@pipeable
def is_quarter_end(col):
    """
    Return True if date is last day of the quarter.
    """
    return col.dt.is_quarter_end

@pipeable
def is_year_start(col):
    """
    Return True if date is first day of the year.
    """
    return col.dt.is_year_start

@pipeable
def is_year_end(col):
    """
    Return True if date is last day of the year.
    """
    return col.dt.is_year_end
