#!/usr/bin/python
#
# Rules:
#  Implement ReversibleLinkedList. A "reversible" linked list is a linked list
#  that can be reversed in place. Do this by implementing the Reverse() call.
#  You can make whatever changes you wish to this code, except you may not:
#
#  1) Alter the parent class in any way.
#  2) Use any built-in or library reverse functions you might find.
#  3) Allow Reverse() to take more than O(N) time.
# 
# The goal:
#  Make the tests pass. To run the tests, make sure this file is called
#  reversible_linked_list.py and is in the same directory as 
#  reversible_linked_list_test.py, then:
#     python reversible_linked_list_test.py
# 
#  Desired output is:
#
# % python reversible_linked_list_test.py                                      
#
# .............
# ----------------------------------------------------------------------
# Ran 13 tests in 0.000s
#
# OK
#

from linked_list import *


class ReversibleLinkedList(LinkedList):
  def Reverse(self):
    """Reverses a linked list in place.

    Args:
      No arguments.

    Returns:
      self for method chaining.
    """
    return self
