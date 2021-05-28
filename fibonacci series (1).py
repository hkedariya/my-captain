#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def fibonacci(n):
    if n==0:
     return 0
    elif n==1:
     return 1
    else:
     return fibonacci(n-2)+ fibonacci(n-1)
n=int(input("Enter the no terms "))
for i in range(n):
 print(fibonacci(i))

   input() 


# In[ ]:




