# Big O Notation 

## Source for reference 

[Big O Notations](https://www.youtube.com/watch?v=V6mKVRU1evU)
[Standford Explaination about Big O Notation](https://www.youtube.com/watch?v=iOq5kSKqeR4)


## O(1)
It means the value of T(n) is bounded by a value that does not depend on the size of input. 

**Examples**
- Access any single element in an array using index 
- Find the minimal value in an array sorted in ascending order (It's the first element, therefore similar to the previous one) 



## O(logn)
It's highly efficient, as the ratio of the number of operations to the size of input decreases and tends to zero as n increases. **Note**: An algorithm that must access all elements of its input cannot take logarithmic time, as the time taken for reading an input of size n is of the order of n. 

The most common example with O(logn) is binary search. 


## &Omega;(1)--> best case 
Take the binar search as an example. If the number we want to find is in the middle of the sorted array, we can find it only be one search, which delivers a running time of 1. On the other hand, if the number we want to find at the end of the array, we need to find it by logn. Therefore, we can use &Omega;(1) to show the best case and O(logn) to show the worset case.

