#!/usr/bin/python

import unittest
import priority_linked_list as pll

class TestPriorityLinkedList(unittest.TestCase):

  def testSimpleAdd(self):
    list = pll.PriorityLinkedList()
    list.Add(1)

    self.assertEqual(list.ToString(), "[1]")

    list.Add(10)
    list.Add(5)
    list.Add(15)
    list.Add(20)
    list.Add(16)

    self.assertEqual(list.ToString(), "[1,5,10,15,16,20]")

  def testInsertFirst(self):
    list = pll.PriorityLinkedList()
    list.Add(10)

    list.Add(1)

    self.assertEqual(list.ToString(), "[1,10]")

  def testInsertSame(self):
    list = pll.PriorityLinkedList()
    list.Add(20)
    list.Add(25)
    list.Add(23)
    list.Add(26)
    list.Add(23)

    self.assertEqual(list.ToString(), "[20,23,23,25,26]")

  # Behaviors copied in from linked_list_test that should still work.
  def testInit(self):
    list1 = pll.PriorityLinkedList()
    self.assertTrue(list1.IsEmpty())

  def testIsEmpty(self):
    list1 = pll.PriorityLinkedList()
    list2 = pll.PriorityLinkedList()

    self.assertTrue(list1.IsEmpty())
    self.assertTrue(list2.IsEmpty())

    list1.Add(10)

    self.assertFalse(list1.IsEmpty())
    self.assertTrue(list2.IsEmpty())

    list2.Add(20)

    self.assertFalse(list1.IsEmpty())
    self.assertFalse(list2.IsEmpty())

  def testGetFront(self):
    list1 = pll.PriorityLinkedList()
    list1.Add(10)

    self.assertEqual(list1.GetFront(), 10)

    list1.Add(20)
    self.assertEqual(list1.GetFront(), 10)

  def testRemoveFront(self):
    list1 = pll.PriorityLinkedList()
    list1.Add(10)

    self.assertEqual(list1.GetFront(), 10)

    list1.Add(20)
    self.assertEqual(list1.GetFront(), 10)

    list1.RemoveFront()
    self.assertEqual(list1.GetFront(), 20)

    list1.Add(4)
    list1.Add(3)
    list1.Add(5)
    self.assertEqual(list1.GetFront(), 3)

    list1.RemoveFront()
    self.assertEqual(list1.GetFront(), 4)

  def testFind(self):
    list1 = pll.PriorityLinkedList()

    self.assertFalse(list1.Find(10))

    list1.Add(10)
    list1.Add(20)
    list1.Add(30)
    list1.Add(40)

    self.assertTrue(list1.Find(10))
    self.assertTrue(list1.Find(20))
    self.assertTrue(list1.Find(40))
    self.assertFalse(list1.Find(0))

  def testRemoveValue(self):
    list1 = pll.PriorityLinkedList()

    self.assertFalse(list1.RemoveValue(10))

    list1.Add(10)
    list1.Add(20)
    list1.Add(25)
    list1.Add(30)
    list1.Add(40)

    self.assertTrue(list1.RemoveValue(10))
    self.assertEqual(list1.GetFront(), 20)

    self.assertTrue(list1.RemoveValue(40))
    self.assertFalse(list1.Find(40))

    self.assertTrue(list1.RemoveValue(25))
    self.assertFalse(list1.Find(25))

if __name__ == '__main__':
  unittest.main()
