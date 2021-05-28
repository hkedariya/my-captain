#!/usr/bin/env python
# coding: utf-8

# In[1]:


def print_positives(arr : list) -> None:
	for val in arr:
		if val > 0:
			print(val)


# In[8]:


print("Enter the values of list1")
list1=list(map(int,input().split()))
print(list1)
x1 = print_positives(list1)


# In[9]:


print("Enter the values of list2")
list2=list(map(int,input().split()))
print(list2)
x2 = print_positives(list2)

input()
# In[ ]:




