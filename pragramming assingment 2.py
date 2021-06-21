#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Ans 1


# In[4]:


km = float(input())
mile=km*0.62
mile


# In[ ]:


#Ans 2


# In[7]:


cel=float(input())
fh= (cel*1.8)+32
print("this is th fahrenheight",fh)


# In[8]:


#Ans 3


# In[10]:


import calendar


# In[13]:


year=int(input())
month=int(input())
mycal=calendar.month(year,month)
print(mycal)


# In[14]:


#Ans 4


# In[15]:


import cmath


# In[16]:


#solve the quadratic equation ax**2+bx+c=0


# In[18]:


a=float(input())
b=float(input())
c=float(input())
d=(b**2)-(4*a*c)
sol=((-b-cmath.sqrt(d)))/(2*a)
sol1=(-b-cmath.sqrt(d))/(2*a)
print(sol,sol1)


# In[19]:


#Ans5


# In[20]:


a=4
b=5


# In[21]:


a,b=b,a


# In[22]:


a,b


# In[23]:


print(a,b)


# In[24]:


a=a+b
b=a-b
a=a-b


# In[25]:


a,b


# In[ ]:




