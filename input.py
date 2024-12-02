#!/usr/bin/env python
# coding: utf-8

# In[ ]:


birthplace = input()
job = input()

# Modify the following line
child_bio_str = (
    'Cam is 6 years old and lives in {0}. '
    'Her favorite color is green and she wants to be a {1} when she grows up.'
)

# format() replaces the curly braces in a string with variables.
# This method is being used to test your code.
new_str = child_bio_str.format(birthplace, job)
print(new_str)


# In[ ]:


The following code outputs a string using values read from input, but the program contains a line with more than 80 columns. Use implicit line joining to join the long string in child_bio_str so that the program does not contain any lines with more than 80 columns.




# In[ ]:


# Read input values
first_name = input("Enter the first name: ")
last_name = input("Enter the last name: ")
age = input("Enter the age: ")

# Long string split using implicit line joining
profile_description = (
    "Name: {0} {1}. "
    "Age: {2}. "
    "This person is a valued member of our community and has "
    "contributed significantly to various projects and initiatives."
)

# format() replaces the curly braces in a string with variables.
formatted_description = profile_description.format(first_name, last_name, age)
print(formatted_description)


# In[ ]:




