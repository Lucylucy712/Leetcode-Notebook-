# Built-in Class in Python 

**immutable**: A class is immutable if each object of that class has a fixed value upon instantation that cannot subsequently be changed. For example, the float class is immutable. 


![image](https://user-images.githubusercontent.com/38546128/110515381-f6ab3b00-80cd-11eb-80dd-f298ff30b387.png)


## The bool Class

`bool(foo)`: Create a Boolean value from a nonboolean type. 

1. Numbers evalutes to *False* if zero, and *True* if nonzero

2. Sequences and other container types evalute to *False* if empty and *True* if nonempty. 


## The int Class

Represent integer values with arbitrary magnitude. 

`int()` returns value *0* by default.

`int(float_number)` returns the truncated value of the float_number. For example: 

1. `int(3.14) = int(3.99) = 3`

2. `int(-3.9) = 03`

`int(str)` returns the the integral value the string is presumed to represent. And it can also custom a different base

`int("137") = 137`

`int("7f",16) = 127`


However, if an invalide string is given, it would raise a ValueError. 


## The float Class 

`float()` return value *0.0*

`float(2)` returns value *2.0*

`float("3.14)` attempts to parse the string as a floating-point value, raising a ValueError as an exception


## Sequence Types: The list, tuple, and str Classes 

*Sequences types* in Python represent a collection of values in which the order is significant. 

We would cover them one by one in more details. 

## Set and forzenset Classes 

### set class : `{"red","green","blue"}`

As the defination in math, set class represents a collection of elements, without duplicates and without any inherent order to those elements. 

**Two restrictions:**

1. No order for those elements 
2. Only instrances of immutable types can be added to a Python set. Only integers, floating-point numbers, and character strings. 

`set()` constructs an empty set 

`{}` *means an empty dictionary*


### frozenset class
It's just an immutable form of the set type. 

## Dict Class 
It's a mapping from a set of distinct keys to associated values. 






