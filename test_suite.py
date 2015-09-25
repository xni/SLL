import random
import unittest

from single_linked_list import (SingleLinkedList, InvalidPositionError,
    NodeIsUnreachableError)
from single_linked_set import SingleLinkedSet


class SingleLinkedListBaseTest(unittest.TestCase):

    def test_initialization(self):
        # empty constructor
        l = SingleLinkedList()

        # construct from list
        l = SingleLinkedList([1, 2, 3, 4, 5])

        # construct from iterable
        l = SingleLinkedList(range(10))

    def test_contains(self):
        l = SingleLinkedList()
        self.assertFalse(l.contains(0))
        self.assertFalse(l.contains(1))
        self.assertFalse(l.contains(None))

        l = SingleLinkedList([1, 2, 3])
        self.assertTrue(l.contains(1))
        self.assertTrue(l.contains(2))
        self.assertTrue(l.contains(2.0))
        self.assertTrue(l.contains(3))
        self.assertFalse(l.contains(4))
        self.assertFalse(l.contains(-1))
        self.assertFalse(l.contains(None))
        self.assertFalse(l.contains({'some': 'datatype'}))
        self.assertFalse(l.contains(2.01))

    def test_get_by_index(self):
        count = 10
        l = SingleLinkedList(100 * i for i in range(count))
        indices = list(range(count))
        random.shuffle(indices)
        for random_index in indices:
            value = l.get_n_th_node(random_index).value
            self.assertEqual(100 * random_index, value)

    def test_repr(self):
        l = SingleLinkedList(['a', 'b', 20])
        self.assertEqual("SingleLinkedList(['a', 'b', 20])", repr(l))

    def test_empty(self):
        l = SingleLinkedList()
        self.assertTrue(l.empty())
        l = SingleLinkedList([0])
        self.assertFalse(l.empty())

    def test_insert_first_element_to_empty_list(self):
        l = SingleLinkedList()
        l.insert_at_position(0, 'D')
        self._check_is_single_element_list(l)

        l = SingleLinkedList()
        l.insert_at_position(-1, 'D')
        self._check_is_single_element_list(l)

    def test_insert_at_position(self):
        l = SingleLinkedList([9, 6, 5])
        l.insert_at_position(0, -3)
        self._check_list(l, (-3, 9, 6, 5))
        l.insert_at_position(0, -4)
        self._check_list(l, (-4, -3, 9, 6, 5))
        l.insert_at_position(1, -5)
        self._check_list(l, (-4, -5, -3, 9, 6, 5))
        l.insert_at_position(4, -6)
        self._check_list(l, (-4, -5, -3, 9, -6, 6, 5))
        l.insert_at_position(7, -7)
        self._check_list(l, (-4, -5, -3, 9, -6, 6, 5, -7))

    def test_insert_after(self):
        l = SingleLinkedList([1])
        node = l.get_n_th_node(0)
        l.insert_after(node, 2)
        self._check_list(l, (1, 2))
        l.insert_after(node, 3)
        self._check_list(l, (1, 3, 2))
        l.insert_after(l.get_n_th_node(2), 7)
        self._check_list(l, (1, 3, 2, 7))

    def test_insert_before(self):
        l = SingleLinkedList([1])
        node = l.get_n_th_node(0)
        l.insert_before(node, 5)
        self._check_list(l, (5, 1))
        l.insert_before(node, 4)
        self._check_list(l, (5, 4, 1))
        l.insert_before(l.get_n_th_node(0), 9)
        self._check_list(l, (9, 5, 4, 1))
        l.insert_before(l.get_n_th_node(2), 12)
        self._check_list(l, (9, 5, 12, 4, 1))

    def test_insert_before_by_reordering(self):
        l = SingleLinkedList([1])
        node = l.get_n_th_node(0)
        l.insert_before_by_reordering(node, 3)
        self._check_list(l, (3, 1))
        l.insert_before_by_reordering(node, 5)
        self._check_list(l, (5, 3, 1))
        node = l.get_n_th_node(2)
        node = l.insert_before_by_reordering(node, 8)
        self._check_list(l, (5, 3, 8, 1))
        node = l.insert_before_by_reordering(node, 6)
        self._check_list(l, (5, 3, 8, 6, 1))

    def test_exceptions(self):
        l1 = SingleLinkedList([1])
        l2 = SingleLinkedList([1])

        l1_node = l1.get_n_th_node(0)
        self.assertRaises(NodeIsUnreachableError,
                          l2.insert_before, l1_node, 3)
        self.assertRaises(InvalidPositionError,
                          l1.insert_at_position, 100, 100)
        self.assertRaises(InvalidPositionError,
                          l1.get_n_th_node, 1)

    def _check_is_single_element_list(self, l):
        self.assertEqual('D', l._head.value)
        self.assertEqual('D', l._tail.value)
        self.assertEqual(None, l._head.next)
        self.assertEqual(None, l._tail.next)
        self.assertEqual("SingleLinkedList(['D'])", repr(l))

    def _check_list(self, l, t):
        cur = l._head
        for expected_value in t:
            self.assertEqual(expected_value, cur.value)
            cur = cur.next
        self.assertEqual(None, cur)
        self.assertEqual(t[-1], l._tail.value)
        self.assertEqual(None, l._tail.next)


class SingleLinkedSetBaseTest(unittest.TestCase):

    def test_initialisation(self):
        s = SingleLinkedSet()
        s = SingleLinkedSet([1, 2, 3])
        s = SingleLinkedSet([1, 1, 1])

    def test_main_features(self):
        s = SingleLinkedSet()
        self.assertFalse(s.contains(1))

        s = SingleLinkedSet([1, 1, 1, 1, 1])
        self.assertTrue(s.contains(1))
        self.assertFalse(s.contains(2))

        s = SingleLinkedSet()
        s.add(2)
        self.assertTrue(s.contains(2))
        self.assertFalse(s.contains(1))
        s.add(1)
        self.assertTrue(s.contains(1))
        self.assertTrue(s.contains(2))

    def test_uniqueness(self):
        s = SingleLinkedSet()
        for _ in range(100):
            # as we didn't do random.seed, this test is easy to reproduce.
            s.add(random.randint(0, 5))

        # as list does not have any public methods to inspect it's size,
        # we will use `get_n_th_node`.
        self.assertRaises(InvalidPositionError,
                          s._container.get_n_th_node, 7)


if __name__ == '__main__':
    unittest.main()

