#!/usr/bin/env python
# coding: utf-8

# In[1]:


numbers = list(range(1,101))

for i in numbers:
    if i%15 == 0:
        n=numbers.index(i)
        numbers.insert(n,"FizzBuzz")
        numbers.remove(n+1)
    elif i%5 == 0:
        m=numbers.index(i)
        numbers.insert(m,"Buzz")
        numbers.remove(m+1)
    elif i%3 == 0:
        a=numbers.index(i)
        numbers.insert(a,"Fizz")
        numbers.remove(a+1)
        
print(numbers)

# https://github.com/eminbulbul/phyton_assigments


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




