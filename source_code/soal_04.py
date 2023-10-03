class stack:
    def__init__(self) :
        self._data = []

def push(self,item) :
    self._data.append(item)

def is_empty(self) :
    return len(self._data)==0

def pop(self) :
    if self.is_empty() :
        raise empty('stack is empty')
    return self._data.pop()