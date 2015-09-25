#!/usr/bin/env python3

import logging
import timeit
import sys


logger = logging.getLogger(__name__)


def do_benchmark():
    number = 100000

    logger.info('Checking insert_at_position 0')
    timer = timeit.Timer(
        'l.insert_at_position(0, 7)',

        'from single_linked_list import SingleLinkedList;'
        'l = SingleLinkedList()')
    measurements = timer.repeat(number=number)
    logger.debug('%s', measurements)

    logger.info('Checking insert_at_position -1')
    timer = timeit.Timer(
        'l.insert_at_position(-1, 7)',

        'from single_linked_list import SingleLinkedList;'
        'l = SingleLinkedList()')
    measurements = timer.repeat(number=number)
    logger.debug('%s', measurements)

    logger.info('Checking insert_at_position 5')
    timer = timeit.Timer(
        'l.insert_at_position(5, 7)',

        'from single_linked_list import SingleLinkedList;'
        'l = SingleLinkedList([1,2,3,4,5])')
    measurements = timer.repeat(number=number)
    logger.debug('%s', measurements)

    logger.info('Checking insert_at_position 14')
    timer = timeit.Timer(
        'l.insert_at_position(14, 7)',

        'from single_linked_list import SingleLinkedList;'
        'l = SingleLinkedList([1] * 50)')
    measurements = timer.repeat(number=number)
    logger.debug('%s', measurements)

    logger.info('Checking insert_after')
    timer = timeit.Timer(
        'l.insert_after(node, 8)',

        'from single_linked_list import SingleLinkedList;'
        'l = SingleLinkedList([1] * 50); node = l.get_n_th_node(5)')
    measurements = timer.repeat(number=number)
    logger.debug('%s', measurements)

    logger.info('Checking insert_after last element')
    timer = timeit.Timer(
        'l.insert_after(node, 8)',

        'from single_linked_list import SingleLinkedList;'
        'l = SingleLinkedList([1]); node = l.get_n_th_node(0)')
    measurements = timer.repeat(number=number)
    logger.debug('%s', measurements)

    logger.info('Checking insert_before [10 Times shorter!]')
    timer = timeit.Timer(
        'l.insert_before(node, 8)',

        'from single_linked_list import SingleLinkedList;'
        'l = SingleLinkedList([1] * 50); node = l.get_n_th_node(5)')
    measurements = timer.repeat(number=int(number / 10))
    logger.debug('%s', measurements)

    logger.info('Checking insert_before first element')
    timer = timeit.Timer(
        'l.insert_before(l.get_n_th_node(0), 8)',

        'from single_linked_list import SingleLinkedList;'
        'l = SingleLinkedList([1] * 50)')
    measurements = timer.repeat(number=number)
    logger.debug('%s', measurements)

    logger.info('Checking insert_before_by_reordering')
    timer = timeit.Timer(
        'l.insert_before_by_reordering(node, 8)',

        'from single_linked_list import SingleLinkedList;'
        'l = SingleLinkedList([1] * 50); node = l.get_n_th_node(40)')
    measurements = timer.repeat(number=number)
    logger.debug('%s', measurements)

    logger.info('Checking adding items to set')
    timer = timeit.Timer(
        's.add(1)',

        'from single_linked_set import SingleLinkedSet;'
        's = SingleLinkedSet()')
    measurements = timer.repeat(number=number)
    logger.debug('%s', measurements)


def main():
    setup_logger()
    do_benchmark()


def setup_logger():
    logger.setLevel(logging.DEBUG)
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    logger.addHandler(stdout_handler)


if __name__ == '__main__':
    main()

