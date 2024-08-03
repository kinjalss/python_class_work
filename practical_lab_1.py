#!/usr/bin/env python
# coding: utf-8

# In[65]:

# Kinjal Surve (A-26)

lo = "Python is Easy!!!"
print(str)
print(str[3:9])
print(str[2:17])
print(str[9:17])
print(str[11:13])
print(str[4:])
print(str[-1])
print(str[ :6]) 

#list
list=["orange","apple","cherry"]#mutable
list.append("mango")#to add element at last
print(list)

#tuple
tuple1=("pizza","burger","sandwich")#immutable
tuple2=("coffee","tea")
print(tuple1[ :3])
print(tuple1+tuple2)

#dict
dict={"Name":"Kinjal"}
print(dict)
print(type(lo))
dict1={"Item":"Chocolate","Price":100}
print(dict1)
print(dict1['Item'])
print(dict1['Price'])
a=2.91 

print(int(a))#type conversion

print(round(a))#round of
b=28
print(float(b))



# In[64]:


#str
x=23
type(x)
y=str(x)
type(y)


# In[67]:


#hex
d=123
type(d)
l=hex(d)
type(l)


# In[68]:


#oct
c=290
type(c)
f=oct(c)
type(f)


# In[75]:


#list to tuple
l1=["icecream","juice","orange","strawberry"]
c=tuple(l1)
print(type(c))
print(c)


# In[78]:


my_list=["guava","imli"]
c = tuple(my_list)
print(type(c))
print(c)


# In[80]:


#herons formula
import math
a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
c = float(input("Enter third number:"))
s=(a+b+c)/2
area = (math.sqrt(s*(s-a)*(s-b)*(s-c)))
print("Area of triangle = ",area)


# In[84]:


a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
avg = (a+b)/2
deviation1 = a-avg
deviation2 = b-avg
print("Average= ",avg)
print("Deviation of first number: ",deviation1)
print("Deviation of second number: ",deviation2)


# In[ ]:




