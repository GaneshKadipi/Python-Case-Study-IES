#!/usr/bin/env python
# coding: utf-8

# In[2]:


from random import randint
def roll():
    while True:
        print('Rolling a die : ')
        res=randint(1,6)
        print('Result :',res)
        print('Do you want to play again ?(y/n) : ')
        a=input()
        if a=='y':
            pass
        else:
            break
print('Welcome to rolling a die game !')
roll()
print('Thank you !')


# In[ ]:




