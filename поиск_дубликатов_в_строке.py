#!/usr/bin/env python
# coding: utf-8

# In[75]:


list = input().split()
list2 = []
order_list = sorted(list)
for i in order_list:
    if order_list.count(i) > 1 and i not in list2:
        list2.append(i)
print(*list2)
        


# In[ ]:




