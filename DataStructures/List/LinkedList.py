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
        else:
            temp = self.head
            for _ in iter(lambda: temp, None):
                if temp.next is not None:
                    temp=temp.next
                else:
                    break
            temp.next=new_node
            new_node.next=None

        self.tail=new_node
        self.length+=1


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
my_linked_list.print_list()