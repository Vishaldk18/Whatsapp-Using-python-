#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""" 
    Have you ever wished to automatically wish your friends on their birthdays, 
or send a set of messages to your friend ( or any Whastapp contact! ) automatically at 
a pre-set time, or send your friends by sending thousands of random text on whatsapp!

Using this code you can do all of it and much more!
   
   
Note:In sendwhatmsg Function first enter any valid whatsapp number with country code for e.g +91 For India,after number 
   enter the message that you want to send and then enter the time for e.g. if you want to send message at 2:30 pm enter
   14,30 or at 12:00 am then enter 0,0
    


"""

get_ipython().system('pip install pywhatkit')
import pywhatkit as kit
kit.sendwhatmsg("+9180*******4","Enter Message Here......",12,0)

