# Write a Python program to search a specific item in a singly linked list and return true if the item is found
# otherwise return false.

class Node:
    # Singly linked node
    def __init__(self, data=None):
        self.data = data
        self.next = None
class singly_linked_list:
    def __init__(self):
        # Create an empty list
        self.head = None
        self.tail = None
        self.count = 0
    def iterate_item(self):
        # Iterate the list.
        current_item = self.head
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val
    def append_item(self, data):
        #Append items on the list
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.count += 1
    def search_item(self,val):
        # Search the list
        for node in self.iterate_item():
            if val == node:
                return True
            return False

items = singly_linked_list()
items.append_item('PHP')
items.append_item('Python')
items.append_item('C#')
items.append_item('C++')
items.append_item('Java')

if items.search_item('SQL'):
    print("True")
else:
    print("False")

if items.search_item('C++'):
    print("True")
else:
    print("False")


