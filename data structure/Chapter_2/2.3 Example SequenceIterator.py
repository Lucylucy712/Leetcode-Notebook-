
### write a class with an given data sequence. Each time__next__ is called, 
### the index is incremented, until reaching the end of sequence 


class SequenceIterator():

    def __init__(self,data):
        self._data = data 
        self._index = -1 
    
    def __len__(self):
        return len(self._data)
    
    def __getitem__(self,i):
        return self._data[i]
    
    def __next__(self):
        self._index +=1 
        if self._index < len(self._data):
            return self._data[self._index]
        else:
            raise StopIteration()
    
    def __iter__(self):
        '''By convention, an iterator must return itself as an iterator'''
        return self 


