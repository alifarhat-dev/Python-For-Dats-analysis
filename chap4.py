import numpy as np

data = np.array(
    [
        [1, 2], 
        [3, 4], 
        [5, 6]]
    )


#scalar mult
data = 2*data
#data.shape (3,2)
#data.dtype int64


#np.zeros array of zeroes
zeros = np.zeros((3,4)) #3 rows and 4 columns


#zeroes_like
zeros_like = np.zeros_like(data) #same shape and dtype as data
#ones and ones_like same principle


#arrage range from 0 to L - 1
R = np.arange(10)

#np.eye 
R = np.eye(4,4)

#np.identity fro square
R = np.identity(4)


#np.array(somthing,dtype = np.) exemple
R = np.array(data,dtype = np.int64)


###==================================###
#Slicing and Indexing

#!Note:
#An important first dis
#tinction from lists is that array slices are views on the original array. This means that
#the data is not copied, and any modifications to the view will be reflected in the source
#array


#The boolean array must be of the same length as the axis it’s indexing. You can even
#mix and match boolean arrays with slices or integers (or sequences of integers, more
#on this later):
#In [89]: data[names == 'Bob', 2:]
#Out[89]: 
#array([[-0.2349,  1.2792],



R = data.T #transpose of the array
R = np.dot(data.T, data) #dot product of the transposed array and the original array







###==========================###
###Universal Functions: Fast Element-Wise Array Functions
##np.exp, np.sqrt, np.add, np.maximum, etc. are all examples of universal functions (ufuncs). These functions operate element-wise on arrays, and they are optimized for performance.
##Some fnuctions
    # abs, fabs
    # sqrt
    # square
    # exp
    # log, log10, log2, log1p
    # sign
    # ceil
    # floor
    # rint
    # modf
    # isnan
    # isfinite, isinf
    # cos, cosh, sin, sinh,
    # tan, tanh
    # arccos, arccosh, arcsin,
    # arcsinh, arctan, arctanh
    # logical_not
    # Compute the absolute value element-wise for integer, floating point, or complex values.
    # Use fabs as a faster alternative for non-complex-valued data
    # Compute the square root of each element. Equivalent to arr ** 0.5
    # Compute the square of each element. Equivalent to arr ** 2
    # Compute the exponent ex of each element
    # Natural logarithm (base e), log base 10, log base 2, and log(1 + x), respectively
    # Compute the sign of each element: 1 (positive), 0 (zero), or -1 (negative)
    # Compute the ceiling of each element, i.e. the smallest integer greater than or equal to
    # each element
    # Compute the floor of each element, i.e. the largest integer less than or equal to each
    # element
    # Round elements to the nearest integer, preserving the dtype
    # Return fractional and integral parts of array as separate array
    # Return boolean array indicating whether each value is NaN (Not a Number)
    # Return boolean array indicating whether each element is finite (non-inf, non-NaN) or
    # infinite, respectively
    # Regular and hyperbolic trigonometric functions
    # Inverse trigonometric functions
    # Compute truth value of not x element-wise. Equivalent to -arr.
    
    
    
# Table 4-4. Binary universal functions
# Function
# Description
# add
# subtract
# multiply
# divide, floor_divide
# power
# maximum, fmax
# minimum, fmin
# mod
# copysign
# Add corresponding elements in arrays
# Subtract elements in second array from first array
# Multiply array elements
# Divide or floor divide (truncating the remainder)
# Raise elements in first array to powers indicated in second array
# Element-wise maximum. fmax ignores NaN
# Element-wise minimum. fmin ignores NaN
# Element-wise modulus (remainder of division)
# Copy sign of values in second argument to values in first argument





# Function
# greater, greater_equal,
# less, less_equal, equal,
# not_equal
# logical_and,
# logical_or, logical_xor
# Description
# Perform element-wise comparison, yielding boolean array. Equivalent to infix operators
# >, >=, <, <=, ==, !=
# Compute element-wise truth value of logical operation. Equivalent to infix operators &
# |, ^





#  The np.meshgrid function takes two 1D arrays and pro
# duces two 2D matrices corresponding to all pairs of (x, y) in the two arrays





# n [145]: result = np.where(cond, xarr, yarr)
# In [146]: result
# Out[146]: array([ 1.1,  2.2,  1.3,  1.4,  2.5])
# The second and third arguments to np.where don’t need to be arrays; one or both of
# them can be scalars. A typical use of where in data analysis is to produce a new array of
# values based on another array. Suppose you had a matrix of randomly generated data
# and you wanted to replace all positive values with 2 and all negative values with -2.
# This is very easy to do with np.where:



##Mathematical and Statistical Methods
arr = np.random.randn(5,4)
arr.mean() #mean of all elements
arr.mean(axis = 0) #mean of each column
arr.mean(axis = 1) #mean of each row



arr.sum() #sum of all elements
arr.sum(axis = 0) #sum of each column
arr.sum(axis = 1) #sum of each row

arr.cumsum() #cumulative sum of all elements
arr.cumsum(axis = 0) #cumulative sum of each column
arr.cumsum(axis = 1) #cumulative sum of each row



arr.cumprod() #cumulative product of all elements
arr.cumprod(axis = 0) #cumulative product of each column
arr.cumprod(axis = 1) #cumulative product of each row


arr.std() #standard deviation of all elements
arr.std(axis = 0) #standard deviation of each column
arr.std(axis = 1) #standard deviation of each row

arr.var() #variance of all elements
arr.var(axis = 0) #variance of each column
arr.var(axis = 1) #variance of each row




