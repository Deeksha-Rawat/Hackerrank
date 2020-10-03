'''
A linked list is said to contain a cycle if any node is visited more than once while traversing the list. 
Given a pointer to the head of a linked list, determine if it contains a cycle. 
If it does, return 1. Otherwise, return 0.
'''


# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next

# Function
def has_cycle(head):
    n1 = head
    n2 = head
    while n1 != None and n1.next != None:
        n1 = n1.next.next
        n2 = n2.next

        if n1 == n2:
            return True
    return False
