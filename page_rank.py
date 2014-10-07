
# coding: utf-8

# In[27]:

import numpy as np


# In[280]:

# Q1

b = 0.7
n = 3
N = np.ones((n,1)) / 3;
r = np.ones((n,1)) / 3;

M = np.array([
        [  0,   0,   0],
        [0.5,   0,   0],
        [0.5,   1,   1]], dtype=np.float)

r = np.dot(b*M, r) + ((1-b)/N)

print r


# In[275]:



