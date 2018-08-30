# -*- coding: utf-8 -*-

from cdl.core import add_lists

def test_add_two_lists():
    list1 = [1, 2]
    list2 = [3, 4]
    assert add_lists(list1, list2)==[4, 6]
