class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print current.data,
            current = current.next

    def insert(self, head, data):
        # Complete this method
        node = Node(data)
        if head == None:
            head = node
        else:
            current = head
            while current.next:
                current = current.next
            current.next = node
        return head


mylist = Solution()
