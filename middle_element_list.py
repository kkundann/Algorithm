class Node():
    def __init__(self,data,next):
        self.data=data
        self.next=next

a1 = Node("India", None)
a2 = Node("1947", a1)
a3 = Node("Bihar", a2)
a4 = Node("2081", a3)
a5 = Node("Patna", a4)

head = a5

firstp = head
secondp = head

while firstp.next != None and firstp.next.next != None:
  firstp = firstp.next.next
  secondp = secondp.next

print secondp.data

# The running time of finding the middle element  with two pointers is O(n) 
#because once we pass through the entire linked list of n elements, the second pointer is at the middle node already.
