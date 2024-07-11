#!/usr/bin/env python
# coding: utf-8

# In[5]:


# creating a list
list_1=[12,21,23,32,34,43]

#Adding an element to list
list_1.append(44)
print(list_1)

#removing an element from list
list_1.remove(32)
print(list_1)

#modifying an element in the list
list_1[3]=50
print(list_1)

#item from index 2 to index 4 (slicing)
n=list_1[2:5]
print(n)

#inserting an element in the list
list_1.insert(3,64)
print("updated list is :",list_1)



# In[20]:


# tuple
tuple_1 = (90,70,50,30)

# add new element to the tuple
B = 10
tuple_1=tuple_1+(B,)
print(tuple_1)

#searching index
print(tuple_1[1:5])
      
# remove an element form the tuple
tuple_1=tuple_1[:2]+tuple_1[4:]
print(tuple_1)

#modifing a element in the tuple
mod_element=55
tuple_1=tuple_1[:1]+(mod_element,)
print(tuple_1)


# In[10]:


# creating a dictionary
student={"Name":"nobita","class":"eight","Age":14,"Mark":"95%"}
print(type(student))

#adding a key value pair to the dictionary
student["gender"]="male"
print(student)

#removing a key value pair from the dictionary
del student["Age"]
print(student)


# updateing the value in the dictionary
student["Mark"]="92%"
print("Correct percentage ",student)


# In[ ]:




