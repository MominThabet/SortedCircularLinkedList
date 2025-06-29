from Node import Node
class SinglyLinkedList:
  def __init__(self):
    self.head = None

  def from_array(self, arr):
    if not arr:
      return
    self.head = Node(arr[0])
    current = self.head
    for val in arr[1:]:
      current.next = Node(val)
      current = current.next

  def is_non_decreasing(self):
    current = self.head
    while current and current.next:
      if current.data > current.next.data:
        return False
      current = current.next
    return True
  def __str__(self):
    nodes = []
    current = self.head
    while current:
      nodes.append(str(current))
      current = current.next
    return " -> ".join(nodes)


class CircularLinkedList:
  def __init__(self):
    self.head = None

  def from_array(self, arr):
    if not arr:
      return
    self.head = Node(arr[0])
    current = self.head
    for val in arr[1:]:
      current.next = Node(val)
      current = current.next
    current.next = self.head  # Circular link

  def __str__(self):
    if not self.head:
      return ""
    nodes = []
    current = self.head
    while True:
      nodes.append(str(current))
      current = current.next
      if current == self.head:
        break
    return " -> ".join(nodes) + " -> [HEAD]"


class DoublyLinkedList:
  def __init__(self):
    self.head = None

  def from_array(self, arr):
    if not arr:
      return
    self.head = Node(arr[0])
    current = self.head
    for val in arr[1:]:
      new_node = Node(val)
      current.next = new_node
      new_node.prev = current
      current = new_node

  def __str__(self):
    nodes = []
    current = self.head
    while current:
      nodes.append(str(current))
      current = current.next
    return " <-> ".join(nodes)
  
  def reverse(self):
    # traverse all the list from start to end and swap next and prev
    current = self.head
    prev_node = None
    while current:
      current.prev, current.next = current.next, current.prev
      prev_node = current
      current = current.prev
    
    self.head = prev_node
    return self
    
      
  
class CircularDoublyLinkedList:
  def __init__(self):
    self.head = None

  def from_array(self, arr):
    if not arr:
      return
    self.head = Node(arr[0])
    current = self.head
    for val in arr[1:]:
      new_node = Node(val)
      current.next = new_node
      new_node.prev = current
      current = new_node
    current.next = self.head
    self.head.prev = current

  def __str__(self):
    if not self.head:
      return ""
    nodes = []
    current = self.head
    while True:
      nodes.append(str(current))
      current = current.next
      if current == self.head:
        break
    return " <-> ".join(nodes) + " <-> [HEAD]"


class SortedCircularLinkedList():
  def __init__(self):
    self.head = None

  def __str__(self):
    if not self.head:
      return ""
    nodes = []
    current = self.head
    while True:
      nodes.append(str(current))
      current = current.next
      if current == self.head:
        break
    return " -> ".join(nodes) + " -> [HEAD]"
  
  def insert(self,data):
    new_node = Node(data)

    # insert in a sorted way
    if self.head is None :
      self.head = new_node
      new_node.next = self.head
      return self
    
    prev = None
    current = self.head
    #  Insert before head (new min value)
    if data < self.head.data :
      # Move to the last node to fix circular link
      while current.next != self.head:
        current = current.next
      current.next = new_node 
      new_node.next = self.head
      self.head = new_node
      return self
    #  Insert in the middle or end

    while current.next != self.head and current.next.data < data:
      current = current.next
    new_node.next = current.next
    current.next = new_node  
    return self