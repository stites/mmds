
# coding: utf-8

# In[27]:

import numpy as np


# In[421]:

# Q1

b = 0.7
n = 3
N = np.ones((n,1)) / 3;
r = np.ones((n,1));

M = np.array([
        [  0,   0,   0],
        [0.5,   0,   0],
        [0.5,   1,   1]], dtype=np.float)

r = np.dot(b*M, r) + ((1-b)/N)

print r


# In[484]:


r = np.dot(b*M, r) + ((1-b)/N)

print r


# In[486]:

r = r / 3
a = r[0][0]
b = r[1][0]
c = r[2][0]

print 'a + b = ', a + b
print 'a + b = ', a + b
print 'b + c = ', b + c
print 'a + c = ', a + c


# In[486]:



