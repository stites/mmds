
# coding: utf-8

# In[27]:

import numpy as np


# In[33]:

# Q1

b = 0.7
n = 3
N = np.empty((n,n))
N.fill(1/n)
M = np.array([
        [0, 0.5, 0.5],
        [0,   0,   1],
        [0,   0,   1]], dtype=np.float)
A = b*M + (1-b)*N
print A


# In[18]:



