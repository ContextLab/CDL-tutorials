# -*- coding: utf-8 -*-
import numpy as np
from .helpers import add

def add_lists(list1, list2):
    """
    Add two lists of integers element-wise

    Parameters
    ----------
    list1 : list
      The first list
    list2 : list
      The second list

    Returns
    -------
    list
      Element-wise sum of the two lists
    """
    return [add(l1, l2) for l1, l2 in zip(list1, list2)]

def add_arrays(arr1, arr2):
    """
    Add two arrays of integers element-wise

    Parameters
    ----------
    arr1 : numpy.ndarray
      The first array
    arr2 : numpy.ndarray
      The second array

    Returns
    -------
    list
      Element-wise sum of the two arrays
    """
    return np.add(arr1, arr2)
