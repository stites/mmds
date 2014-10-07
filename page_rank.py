
# coding: utf-8

# In[488]:

import numpy as np


# In[493]:

def get_pagerank (b, n, M, iters, scale):
    N = np.ones((n,1)) / n;
    r = np.ones((n,1));
    for x in xrange(iters):
        r = np.dot(b*M, r) + ((1-b)/N)
    r = r / scale
    return r
    


# In[494]:

# Q1
r = get_pagerank(0.7,
                 3,
                 np.array([
                    [  0,   0,   0],
                    [0.5,   0,   0],
                    [0.5,   1,   1]], dtype=np.float),
                 1000,
                 3)
a = r[0][0]
b = r[1][0]
c = r[2][0]

print 'a + b = ', a + b
print 'a + b = ', a + b
print 'b + c = ', b + c
print 'a + c = ', a + c


# In[517]:

#Q2
r = get_pagerank(0.85,
                 3,
                 np.array([
                    [  0,   0,   1],
                    [0.5,   0,   0],
                    [0.5,   1,   0]], dtype=np.float),
                 10000,
                 1)

a = r[0][0]
b = r[1][0]
c = r[2][0]

print 'a ', a
print 'b ', b
print 'c ', c

print '      c = %0.3f b + %0.3f a' % (b/c, a/c)
print '      b = %0.3f a + %0.3f c' % (a/b, c/b)
print ' 0.95 b = %0.3f a + %0.3f c' % ((a/b)*0.95, (c/b)*0.95)
print '%0.3f c =       b + %0.3f a' % (c/b, a/b)



# In[498]:




# In[491]:



