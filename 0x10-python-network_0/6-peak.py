#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers

    Args:
        list_of_integers (list): list of unsorted integers
    """
    if not len(list_of_integers):
        return None

    no_dup = list(set(list_of_integers))
    return sorted(no_dup)[-1]
