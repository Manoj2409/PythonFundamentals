from distutils.core import setup_keywords
from operator import truediv, index


class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value):
        node=Node(value)
        self.head=node
        self.tail=node
        self.length=1

    def print_list(self):
        temp = self.head
        for node in iter(lambda: temp, None):
            print(node.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1

    def pop(self):
        if self.length==0:
            print("Has no elements")
            return
        elif self.length==1:
            self.head=None
            self.tail=None
        else:
            temp=self.head
            for _ in iter(lambda : temp,None):
                if temp.next.next is None:
                    break
                temp=temp.next
            self.tail=temp
            temp2=temp.next
            temp.next=None
        self.length-=1
        return temp2

    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        elif self.length>0:
            #if the length is greater than zero
            temp_head=self.head
            self.head=new_node
            new_node.next=temp_head
        self.length+=1

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self,index):
        if index<0 or index>=self.length:
            print("Index should be within range")
            return
        temp=self.head
        for i in range(index):
            temp=temp.next
        return temp

    def set_value(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False

    def insert(self,index,value):
        if index<0 or index>self.length:
            return False
        if index==0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node=Node(value)
        temp=self.get(index-1)
        new_node.next=temp.next
        temp.next=new_node
        self.length+=1
        return True

    #scenarios for remove
    """
    1. remove first
    2. remove last 
    3. remove inbetween
    
    before that check index within range
    
    """
    def remove(self,index):
        if index<0 or index >=self.length:
            return None

        elif index==0:
            return self.pop_first()

        elif index==self.length-1:
            temp=self.head
            for i in range(index-1):
                temp=temp.next
            temp2=temp.next
            temp.next=None
            self.length-=1
            return temp2

        else:
            temp1=self.get(index-1)
            temp2=temp1.next #value need to be removed
            temp1.next=temp1.next.next
            temp2.next=None
            self.length-=1
            return temp2

    def reverse(self):
            if self.length<=1:
                return
            for i in range(self.length//2):
                temp1=self.get(i).value
                temp2=self.get(self.length-1-i).value
                self.set_value(i,temp2)
                self.set_value(self.length-1-i,temp1)



my_linked_list=LinkedList(4)
print(my_linked_list.head.value)
print(my_linked_list.tail.value)
print(my_linked_list.length)
my_linked_list.print_list()



#print after append
print("Print after append")
my_linked_list.append(10)
my_linked_list.append(20)
my_linked_list.append(30)
my_linked_list.append(40)
my_linked_list.print_list()

print("After pop")
my_linked_list.pop()
my_linked_list.print_list()

print("After prepend")
my_linked_list.prepend(123)

my_linked_list.get(4)
my_linked_list.set_value(0,999)
print("Print the list")
my_linked_list.print_list()

print("After reversed")
my_linked_list.reverse()
my_linked_list.print_list()