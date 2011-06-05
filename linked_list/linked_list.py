#!/usr/bin/python
#
# Rules:
#  Implement the missing methods in LinkedList (the ones that have 'pass')
#  as the body. You may make any changes you want, the only constraints are:
#
#  1) You may not change the test code. (talk to me first.)
#  2) You may not use a Python list ([]) or a Python dictionary ({}) anywhere in
#     your code.
#
# The goal:
#  Make the tests pass. To run the tests, make sure this file is called
#  linked_list.py and is in the same directory as linked_list_test.py, then:
#     python linked_list_test.py
# 
#  Desired output is:
#
# % python linked_list_test.py                                      
# .......
# ----------------------------------------------------------------------
# Ran 7 tests in 0.000s
#
# OK
#
#
# I left you a little bit of code to get you started.
#
# A semi-rule:
#  Please do not consult anyone else on this except to ask general Python
#  questions. :)
#

class Node(object):
  def __init__(self, value, next=None):
    """A simple container for a Linked List."""
    self.value = value
    self.next = next


class LinkedList(object):
  def __init__(self):
    """Initializes a new LinkedList."""
    self._head = None

    # Note: you can do this without keeping track of the tail. This variable
    # simplifies a case in Add but makes a case in Remove more complex.
    self._tail = None

  def IsEmpty(self):
    """Returns True if this list is empty, False otherwise."""
    return self._head is None

  def Add(self, val):
    """Adds val to the end of the LinkedList.

    Args:
      val: value to add, can be of any type.

    Returns:
      No return.
    """
    pass

  def GetFront(self):
    """Returns first value in the Linked List."""
    return self._head.value

  def RemoveFront(self):
    """Removes the first value in the Linked List."""
    pass

  def Find(self, value):
    """Finds value in the Linked List.

    Args:
      value: value to find.

    Returns:
      True if value exists in this linked list, False otherwise.
    """
    pass

  def RemoveValue(self, value):
    """Removes the first instance of value in this linked list.

    Note: if 'value' occurs twice (e.g; in a list of h, e, l, l o) this method
    will only remove the FIRST instance of it.

    Args:
      value: value to remove.

    Returns:
      True if the value was found and removed, False otherwise.
    """
    pass

  def ToString(self):
    """Produces a string representation of this list's contents.

    An empty list will return: []
    A list with one value 'h': [h]
    A list with more than 1:   [h,e,l,l,o]

    Returns:
      A string containing the string's internal contents.
    """
    pass
