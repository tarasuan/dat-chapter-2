#!/usr/bin/env python

import numpy as np
from numpy import *

a = arange(100).reshape(10,10)
b = ( [1,3,5] )
c = ( [2,4,6] )
print b+c

d = np.arange(18).reshape(3,6)
print d.ndim
print d.dtype

def retrieve_column(matrix, n):
  print a[:,n]

retrieve_column(array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
       [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]]), 2)