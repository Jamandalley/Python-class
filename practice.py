a = 5
b = 3
c = complex(a, b)
name = "Alice"
age = 30
message_1= "My name is " + name + " and I am " + str(age) + " years old."
print(message_1)
my_name = "Jamandalley"
my_age = 30
my_discipline = "Medical Laboratory Scientist"
current_work_place = "LAUTECH Teaching Hospital"
my_role = "Intern"
current_aspiration = "Data Science and Analytics"
message_2 = "My name is "+my_name+", I am "+str(age)+"years old. By discipline, i am a "+my_discipline+" currently working at "+current_work_place+" as an "+my_role+".However, I am aspiring to become a specialist at "+current_aspiration+" with a view to revolutionizing healthcare practices locally and internationally."
print(message_2)
print(message_2[5])
message_3 = f"My name is {my_name}, I am {my_age} years old. By discipline, i am a {my_discipline} currently working at {current_work_place} as an {my_role}. However, I am aspiring to become a specialist at {current_aspiration} with a view to revolutionizing healthcare practices locally and internationally."
print(message_3)
print(message_3[-3])
print(message_3[-4])
print(message_3[-5])
print(message_3.upper())

"""message.upper() # to convert to uppercase
message.lower() # to convert to lowercase
message.title() # to capitalize the first letter of every word
message.find('p') # returns the index of the first occurrence of p 
 (or -1 if not found) 
message.replace('p', 'q')"""
print(message_3.find('p'))

"""LISTs
numbers = [1, 2, 3, 4, 5]
numbers[0] # returns the first item 
numbers[1] # returns the second item
numbers[-1] # returns the first item from the end
numbers[-2] # returns the second item from the end 

numbers.append(6) # adds 6 to the end
numbers.insert(0, 6) # adds 6 at index position of 0
numbers.remove(6) # removes 6
numbers.pop() # removes the last item
numbers.clear() # removes all the items
numbers.index(8) # returns the index of first occurrence of 8
numbers.sort() # sorts the list
numbers.reverse() # reverses the list
numbers.copy() # returns a copy of the list"""

coordinates = (1, 2, 3)
x, y, z = coordinates
print(x)

# DICTIONARY
# USe to store "Key/value pairs"
customer = {
 name: "John Smith",
 age: 30,
 }
"""
customer[“name”] # returns “John Smith”
customer[“type”] # throws an error 
customer.get(“type”, “silver”) # returns “silver”
customer[“name”] = “new name” """
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x +" "+ y +" " + z)

# COMPLEX NUMBERS 
a = 1
b = 2
c = 3j
d = 4j
z = complex(a, b)
print(z)
print(end="")
print(z.real)


# Python code to demonstrate the working of
# complex(), real() and imag()

# importing "cmath" for complex number operations
import cmath

# Initializing real numbers
x = 5
y = 3

# converting x and y into complex number
z = complex(x,y);

# printing real and imaginary part of complex number
print ("The real part of complex number is : ", end="")
print (z.real)

print ("The imaginary part of complex number is : ", end="")
print (z.imag)

# Python code to demonstrate the working of
# phase()

# importing "cmath" for complex number operations
import cmath

# Initializing real numbers
x = -1.0
y = 0.0

# converting x and y into complex number
z = complex(x,y);

# printing phase of a complex number using phase()
print ("The phase of complex number is : ",end="")
print (cmath.phase(z))
temp = eval(input('Enter a temperature in Celsius: '))
f_temp = 9/5*temp+32
print('In Fahrenheit, that is', f_temp)
# Ask the user to enter a number x. Use the sep optional argument to print out x, 2x, 3x, 4x, and 5x, each separated by three dashes
num1 = eval(input('Enter a number: '))
print("The number you enetered is", num1)
print(num1, 2*num1, 3*num1, 4*num1, 5*num1, sep="---")