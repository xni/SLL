from single_linked_list import SingleLinkedList


class SingleLinkedSet:
    """ Data structure for storing only unique values. 
    
    Not thread-safe.
    """
    def __init__(self, iterable=None):
        self._container = SingleLinkedList()
        if iterable:
            for item in iterable:
                self.add(item)
        
    def add(self, value):
        if not self._container.contains(value):
            self._container.append(value)

    def contains(self, value):
        return self._container.contains(value)

    def __contains__(self, value):
        return self.contains(value)

