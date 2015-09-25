class BaseError(Exception):
    """ Base exception for on exceptions in this module. """


class InvalidPositionError(BaseError):
    """ Raised when wrong position is passed to some functions. """


class NodeIsUnreachableError(BaseError):
    """ Raised when wrong node is passed to some functions. """


class SingleLinkedList:
    """ Container data-structure.
    
    Not thread-safe.
    """

    def __init__(self, iterable=None):
        self._head = None
        self._tail = None

        if iterable:
            for item in iterable:
                self.append(item)

    def append(self, value):
        """ Append new node with `value` to the end of a list.

        Time complexity is O(1).
        """
        return self.insert_at_position(-1, value)

    def insert_at_position(self, position, value):
        """ Method for inserting `value` to `position`.
        
        Position should be in interval [0..N] or it may have a special
        value of `-1` to insert to the end of a list in O(1) operations.

        The value that is currently at `position` is moved forward, to
        `position + 1`.

        Time complexity is:
          - O(1) for inserting to the first or to the last position.
          - O(N) for inserting to some arbitrary position.

        :param position: Integer, position where new element will stand.
        :param value: Object, value to be inserted.
        :raises: InvalidPositionError, in case when list length is
                 less than `position` items.
        """
        new_node = SingleLinkedList.Node(value)
        if self.empty():
            self._head = new_node
            self._tail = new_node
        elif position == 0:
            new_node.next = self._head
            self._head = new_node
        else:
            if position == -1:
                prev = self._tail
            else:
                prev = self.get_n_th_node(position - 1)
            new_node.next = prev.next
            prev.next = new_node
            # This check should be performed either for position = -1 or
            # because position may be equal to list's length.
            self._check_if_tail_updated(new_node)

    def insert_after(self, node, value):
        """ Creates a new node after `node`. Node will contain `value`.

        In case then `node` can not be reached from self._head,
        this function may lead to inconsistency in both self, and `node`
        owner.

        Time complexity is O(1).

        :param node: Node reachable from self._head.
        :param value: Object, value to be inserted.
        """
        new_node = SingleLinkedList.Node(value, node.next)
        node.next = new_node
        self._check_if_tail_updated(new_node)

    def insert_before(self, node, value):
        """ Creates a new node before `node`.

        Time complexity is O(N).

        :param node: Node reachable from self._head.
        :param value: Object, value to be inserted.
        :raises: NodeIsInreachableError, when `node` does not belong
                 to this list.
        """
        new_node = SingleLinkedList.Node(value, node)
        if node == self._head:
            self._head = new_node
        else:
            prev = self._head
            while prev is not None and prev.next != node:
                prev = prev.next
            if prev is None:
                raise NodeIsUnreachableError()
            prev.next = new_node

    def insert_before_by_reordering(self, node, value):
        """ Reorders values in nodes so that `value` is prior to `node.value`.

        THIS METHOD BREAKS YOUR EXPECTATIONS ABOUT `node`.
        >>> a = node.value
        >>> l.insert_before(node, 'foobar')
        >>> b = node.value
        >>> assert a.value == b.value
        AssertionError
        
        Time complexity is O(1).

        :param node: Node reachable from self._head.
        :param value: Object, value to be inserted.
        :return: Node, which contains the value of original `node`.
        """
        self.insert_after(node, value)
        node.value, node.next.value = node.next.value, node.value
        # self._head must not be updated in that case. Because if it was
        # pointing to `node`, after that swap `node` will be interpreted
        # as node.prev.
        return node.next

    def empty(self):
        return self._head is None

    def get_n_th_node(self, required_position):
        position = 0
        node = self._head
        while position < required_position and node is not None:
            position += 1
            node = node.next
        if position == required_position and node is not None:
            return node
        else:
            raise InvalidPositionError()

    def contains(self, value):
        """ Returns True is value is in the list.

        Time complexity is O(N).
        """
        node = self._head
        while node is not None and node.value != value:
            node = node.next
        return node is not None

    def __contains__(self, value):
        return self.contains(value)
    
    def __repr__(self):
        items = []
        node = self._head
        while node is not None:
            items.append(repr(node.value))
            node = node.next
        return 'SingleLinkedList([{values}])'.format(values=', '.join(items))

    def __str__(self):
        return repr(self)

    def _check_if_tail_updated(self, new_node):
        if new_node.next is None:
            self._tail = new_node


    class Node:
        __slots__ = ('value', 'next')

        def __init__(self, value, next=None):
            self.value = value
            self.next = next

