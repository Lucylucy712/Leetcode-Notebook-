


###To demonstrate the use of operator overloading via special methods. 

class Vector:
    
    def __init__(self,d):
        """Create a d-dimensional vector of zeros"""
        self._coords = [0]*d
    
    def __len__(self):
        """Return the dimension of the vector"""
        return len(self._coords)
    
    def __getitem__(self,j):
        """Get the jth coordinate of vector"""
        return self._coords[j]
    
    def __setitem__(self,j,val):
        """Gset jth coordinate of vector to a given value
        """
        self._coords[j] = val
    
    def __add__(self,other):
        """Return sum of two vectors"""
        if len(self)!= len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result 
    
    def __eq__(self,other):
        '''Return True if vector has same coordinates as others'''
        return self._coords == other._coords

    def __ne__(self,other):
        return not self == other ## rely on existing __eq__()
    
    def __str__(self):
        """Produce string representation of vector"""
        return "<" + self._coords[1:-1] + ">"
