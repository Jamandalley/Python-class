print ("Welcome to the first version")
print ("This space will be used by Jamandalley")
""" Variables declarations
Variabke can only use alphanumeric characters
Case-sensitive
Methods of joining variable names in Python
1. Pascal-style names: (e.g. FristNameOfCharacters)
2. Camel-style names: starts with small letter and proceeds with capital letter (e.g. firstNameOfCharacter)
3. Snake casing: uses undercose after each letter (e.g. first_name_of_Character)""" 
#Assignnment: Methods of Concatenation, Types of variabes

"""Data types in Python
1. Numeric (integer, float, complex)
2. Dictionary 
3. Boolean
4. Set
5. Sequence type (strings, list and tuple)
"""
# Concatenation in Python
# 1. String concatenation
string1 = "Hello"
string2 = " world!"
result = string1 + string2
print(result)  # Output: "Hello world!"
# 2. List concatenation
# Using the + operator
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print(result)  # Output: [1, 2, 3, 4, 5, 6]

# Using the .extend() method
list1.extend(list2)  # list1 now contains [1, 2, 3, 4, 5, 6]

#Using Join method: For concatenating large lists, using the .join() method is more efficient than repeatedly using the "+" operator, as the latter creates intermediate objects.
items = ["apple", "banana", "cherry"]
result = ", ".join(items)
print(result)  # Output: "apple, banana, cherry"

# 3. Tupple concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print(result)  # Output: (1, 2, 3, 4, 5, 6)

# 4. String and variable concatenation
name = "Alice"
age = 30
message = "My name is " + name + " and I am " + str(age) + " years old."
print(message)  # Output: "My name is Alice and I am 30 years old."

# 5. Dictionary concatenation
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2) # dict1 now contains {"a": 1, "b": 3, "c": 4}
print(dict1.update(dict2)) 

# F-string concatenation: F-strings, also known as formatted string literals, are a feature introduced in Python 3.6 that provide a concise and convenient way to embed expressions inside string literals. F-strings are defined by prefixing a string literal with the letter "f" or "F" and then enclosing the expressions to be evaluated in curly braces {}.
name = "Jamandalley"
age = 30

# Using f-string to embed variables in a string
message = f"My name is {name} and I am {age} years old."
print(message)

