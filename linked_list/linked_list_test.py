#!/usr/bin/python

import unittest
import linked_list

class TestLinkedList(unittest.TestCase):

  def testInit(self):
    list1 = linked_list.LinkedList()
    self.assertTrue(list1.IsEmpty())

  def testIsEmpty(self):
    list1 = linked_list.LinkedList()
    list2 = linked_list.LinkedList()

    self.assertTrue(list1.IsEmpty())
    self.assertTrue(list2.IsEmpty())

    list1.Add(10)

    self.assertFalse(list1.IsEmpty())
    self.assertTrue(list2.IsEmpty())

    list2.Add(20)

    self.assertFalse(list1.IsEmpty())
    self.assertFalse(list2.IsEmpty())

  def testGetFront(self):
    list1 = linked_list.LinkedList()
    list1.Add(10)

    self.assertEqual(list1.GetFront(), 10)

    list1.Add(20)
    self.assertEqual(list1.GetFront(), 10)

  def testRemoveFront(self):
    list1 = linked_list.LinkedList()
    list1.Add(10)

    self.assertEqual(list1.GetFront(), 10)

    list1.Add(20)
    self.assertEqual(list1.GetFront(), 10)

    list1.RemoveFront()
    self.assertEqual(list1.GetFront(), 20)

  def testFind(self):
    list1 = linked_list.LinkedList()

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
    list1 = linked_list.LinkedList()

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

    list2 = linked_list.LinkedList()
    list2.Add('h')
    list2.Add('e')
    list2.Add('l')
    list2.Add('l')
    list1.Add('o')

    self.assertTrue(list2.RemoveValue('l'))
    self.assertTrue(list2.Find('l'))
    self.assertTrue(list2.RemoveValue('l'))
    self.assertFalse(list2.Find('l'))

  def testToString(self):
    list1 = linked_list.LinkedList()
    self.assertEqual(list1.ToString(), '[]')

    list1.Add('h')
    self.assertEqual(list1.ToString(), '[h]')

    list1.Add('e')
    self.assertEqual(list1.ToString(), '[h,e]')

    list1.Add('l')
    list1.Add('l')
    list1.Add('o')
    self.assertEqual(list1.ToString(), '[h,e,l,l,o]')

if __name__ == '__main__':
  unittest.main()
