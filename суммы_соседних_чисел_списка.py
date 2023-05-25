#!/usr/bin/env python
# coding: utf-8

# In[53]:


list = [int(i) for i in input().split()]
list2 = []
for i in range(len(list)):
    if len(list) == 1:
        list2.append(list[0])
    elif i == 0:
        list2.append(list[1] + list[-1])
    elif i == len(list) - 1:
        list2.append(list[0] + list[-2])
    else:
        list2.append(list[i - 1] + list[i + 1])
print(*list2)

