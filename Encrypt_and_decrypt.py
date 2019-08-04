#!/usr/bin/env python
# coding: utf-8

# In[1]:


__author__ = "Helen"
__date__ = "2019-08-03"


# In[2]:


import requests


# In[3]:


html_result = requests.get("https://gist.githubusercontent.com/simongfxu/13accd501f6c91e7a423ddc43e674c0f/raw/44fa5f348a2c98c04c6d831e02935e3eb48682b0/chinese-words.txt")
#print(html_result.text)


# In[4]:


#html_result.text[200]


# In[5]:


message = input("Please input your message: ")


# In[7]:


# encryption (ord() is suitable for all Unicode characters)
result = []
for char in message:
    result.append(str(ord(char) * 2 + 1000))
result = '|'.join(result)

print("After encryption, the result is: " + result)

# decryption
after_result = ''
result = result.split('|')
for char in result:
    after_result += chr((int(char)-1000) // 2)

print("After decryption, the result is: " + after_result)


# In[ ]:





# In[ ]:




