#!/usr/bin/python
#
# Rules:
#  Implement PriorityLinkedList. A "priority" linked list stores its
#  elements in sorted order. You may make any changes you wish to this
#  code, the only constraints are:
#
#  1) PriorityLinkedList must maintain the same public interface as
#     LinkedList. (PriorityLinkedList is-a LinkedList)
#  2) Insertions into the PriorityLinkedList must be made in no worse
#     than O(N) time.
#  3) You may not use a Python list ([]) or a Python dictionary ({}) anywhere in
#     your code. Nor may you use any sorting library or function.
#
# The goal:
#  Make the tests pass. To run the tests, make sure this file is called
#  priority_linked_list.py and is in the same directory as 
#  priority_linked_list_test.py, then:
#     python priority_linked_list_test.py
# 
#  Desired output is:
#
# % python priority_linked_list_test.py                                      
#
# .........
# ----------------------------------------------------------------------
# Ran 9 tests in 0.000s
#
# OK
#

from linked_list import *

class PriorityLinkedList(LinkedList):
  pass
