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

#Data types in Python
# 1. 
# Concatenation in Python
# 1. String concatenation
string1 = "Hello"
string2 = " world!"
result = string1 + string2
print(result)  # Output: "Hello world!"
# 2. List concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print(result)  # Output: [1, 2, 3, 4, 5, 6]
# 3. Tupple concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print(result)  # Output: (1, 2, 3, 4, 5, 6)
# String and variable concatenation
name = "Alice"
age = 30
message = "My name is " + name + " and I am " + str(age) + " years old."
print(message)  # Output: "My name is Alice and I am 30 years old."
