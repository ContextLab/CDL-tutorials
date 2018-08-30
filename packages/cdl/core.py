# -*- coding: utf-8 -*-
from .helpers import add

def add_lists(list1, list2):
    """
    Add two lists of integers element-wise

    Parameters
    ----------
    list1 : list
      The first list
    y : int
      The second list

    Returns
    -------
    list
      Element-wise sum of the two lists
    """
    return [add(l1, l2) for l1, l2 in zip(list1, list2)]
