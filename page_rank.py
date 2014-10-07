
# coding: utf-8

# In[27]:

import numpy as np


# In[171]:

# Q1

b = 0.7
n = 3
N = np.ones((n,n)) / 3;

M = np.array([
        [0, 0.5, 0.5],
        [0,   0,   1],
        [0,   0,   1]], dtype=np.float)
A = np.add(b*M, (1-b)*N)


# In[151]:



