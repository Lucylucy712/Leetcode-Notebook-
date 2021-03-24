# Stacks

A stack is a collection of objects that are inserted and removed according to the *last-in,first-out* principle. 

A stack is an abstract data type such that an instance *S* supports the following methods: 

- `S.push(e)`: Add element `e` to the top of stack S
- `S.pop()`: remove and return the top element from the stack S. An error would occur if the stack is empty 
- `S.top()`: return the top element from the stack S, without removing it. An error would occus if the stack is empty 
- `S.ie_empty()`: return `True` if stack S does not contain any elements 
- `len(S)`: return the number of elements in stack `S`. 

## Adapter Pattern 

The adapter design pattern applies to any context where we effectively want to modify an existing class so that its methods match those of a related, but different class or interface. 
