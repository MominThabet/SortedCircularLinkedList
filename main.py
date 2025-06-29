from LinkedList import *
from Node import Node 
def main ():
  ll = SinglyLinkedList.from_array(arr=[4,2,7,1,3])
  print(ll)
  print(ll.insertion_sort())
  
def JosephusEliminationGame(n,k):
  cll = CircularLinkedList()
  cll.from_array([i for i in range(1,n+1)])
  # now we shall traverse and delete the kth element
  current = cll.head
  while current.next != current:
    for _ in range(k - 2):  # stop at node before the one to delete
      current = current.next
    print(f"Eliminating: {current.next.data}")
    current.next = current.next.next  # delete k-th node
    current = current.next  # continue from next node
  return f'Remaining:[{current.data}]'

def ListReductionToNonDecreasingOrder(array):
  cl = SinglyLinkedList()
  cl.from_array(array)
  op_count = 0
  
  while not cl.is_non_decreasing():
    # find the leftmost adjacent pair with minimum sum
    min_sum = float('inf') # the max infinity so any actual sum is smaller from it
    prev = None # the node before the current during the traverse
    current = cl.head # the node I am currently at
    min_prev = None #  Will point to the node before the min-sum pair's first node that I will replace

    # Traverse list to find the leftmost adjacent pair with the smallest sum
    while current and current.next:
      pair_sum = current.data + current.next.data
      if pair_sum < min_sum:
        min_sum = pair_sum
        min_prev = prev  # Save the node before the smallest sum pair found so far
      prev = current
      current = current.next

    # replace the pair with their sum
    if min_prev is None :
      # the head and the head.next is the smallest pair sum
      first = cl.head 
      second = first.next
      new_node = Node(first.data + second.data)
      new_node.next = second.next
      cl.head = new_node  # Update head to point to the new merged node
    else :
      first = min_prev.next
      second = first.next
      new_node = Node(first.data + second.data)
      new_node.next = second.next
      min_prev.next = new_node

    op_count += 1
  return op_count

def arrayInsertionSort (array):
  for index in range(1, len(array)):
    temp_value = array[index]
    position = index - 1
    while position >= 0:
      print(array[position], array[index] )
      if array[position] > temp_value:
        array[position + 1] = array[position]
        position = position - 1
      else:
        break
      
      array[position + 1] = temp_value
  return array
  
 

if __name__ == '__main__':
  # print(JosephusEliminationGame(5,3))
  # print(ListReductionToNonDecreasingOrder([5,2,1,3]))
  
  
  
  # dll = DoublyLinkedList()
  # dll.from_array(arr=[4,2,7,1,3])
  # print(dll)
  # dll.reverse()
  # print(dll)

  ## the Assignment to make a sorted circular linked list
  # and insert in sorted way
  scll = SortedCircularLinkedList()
  scll.insert(7)
  scll.insert(3)
  scll.insert(9)
  scll.insert(1)
  scll.insert(4)
  scll.insert(-4)

  print(scll)