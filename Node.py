class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

  def __str__(self):
    return str(self.data)
