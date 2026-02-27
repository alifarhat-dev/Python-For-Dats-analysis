import pandas as pd
from pandas import Series,DataFrame


#Introduction to pandas Data Structures

#Series
arr = Series([1,2,3,4,5]) 
#Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.). The axis labels are collectively referred to as the index. The basic method to create a Series is to call:

#we can also specify an index
arr2 = Series([1,2,3,4,5], index=['a','b','c','d','e'])

# NumPy array operations, such as filtering with a boolean array, scalar multiplication,
# or applying math functions, will preserve the index-value link


# In [15]: obj2[obj2 > 0]      In [16]: obj2 * 2      In [17]: np.exp(obj2)
# Out[15]:                     Out[16]:               Out[17]:             
# d    6                       d    12                d     403.428793     
# b    7                       b    14                b    1096.633158     
# c    3                       a   -10                a       0.006738     
#                              c     6                c      20.085537


#DataFrame
#A DataFrame represents a tabular, spreadsheet-like data structure containing an ordered collection of columns, each of which can be a different value type (numeric, string, boolean, etc.). The DataFrame has both a row and column index; it can be thought of as a dict of Series (or a structured array) and is generally the most commonly used pandas object.

#different ways to create a DataFrame

#1 from a single Series object
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)

frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                     index=['one', 'two', 'three', 'four', 'five'])





#!NOTe The column returned when indexing a DataFrame is a view on the underlying data, not a copy. Thus, any in-place modifications to the Series
# will be reflected in the DataFrame. The column can be explicitly copied
# using the Series’s copy method.

