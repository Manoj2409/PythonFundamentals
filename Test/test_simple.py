from DataStructures.List.LinkedList import LinkedList
import pytest




def test_head():
    linkedlist = LinkedList(10)
    linkedlist.append(12)
    linkedlist.append(13)
    linkedlist.append(14)
    assert linkedlist.head.value == 10

def test_tail():
    linkedlist = LinkedList(10)
    linkedlist.append(12)
    linkedlist.append(13)
    linkedlist.append(14)
    assert linkedlist.tail.value == 14

def test_length():
    linkedlist = LinkedList(10)
    linkedlist.append(12)
    linkedlist.append(13)
    linkedlist.append(14)
    assert linkedlist.length==4

def test_pop():
    linkedlist = LinkedList(10)
    linkedlist.append(12)
    linkedlist.append(13)
    linkedlist.append(14)
    linkedlist.pop()
    assert linkedlist.length == 3

def test_prepend():
    linkedlist = LinkedList(10)
    linkedlist.prepend(12)
    assert linkedlist.head.value==12
    assert linkedlist.length==2