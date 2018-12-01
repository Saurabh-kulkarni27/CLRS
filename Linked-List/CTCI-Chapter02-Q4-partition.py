'''
Problem Statement: Partition a linked list around  a value x, such that all elements < x are on left of x, and all elements >= x are on right side
clarifications:
1) linked list may or may not contain value x
2) linked list is unsorted
3) after partitioning ordering of elements should not change


Logic:
1) maintain two different linked list lets say name small and more
  -- small linked list: store all elements smaller than value x
  -- more : all elements >= val x
2) join these two linked list

other variations of same problem: partition based on even/odd 

Time complexity: O(n) and Space required O(n)
'''


class Node:
    def __init__(self,data):
        self.data = data     #intialize data
        self.next = None     #default next pointer is set to none


class SLL:

    #initialize head with None
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head

        while(temp != None):
            print(temp.data, end='--->')
            temp = temp.next

    def insert_first(self,data):
        node = Node(data)

        if self.head == None:
            self.head = node
            return

        node.next = self.head
        self.head = node


    def insert_end(self,data):

        node = Node(data)

        if self.head == None:
            self.head = node
            return

        else:
            temp = self.head
            while (temp.next != None):
                temp = temp.next
            temp.next = node

    def partition(self,data):
        """

        :rtype: none
        """

        small = SLL()
        more = SLL()

        node = self.head

        while(node):
            #insert in small/more linked list
            if (node.data < data):
                small.insert_end(node.data)
            else:
                more.insert_end(node.data)
            node = node.next

        #traverse to small linked list end so to join the small and more linked list
        p = small.head
        while(p.next):
            p = p.next

        p.next = more.head
        #partitioned linked list
        print('partitioned linked')
        small.print_list()



if __name__=='__main__':
    obj = SLL()

    obj.insert_end(10)
    obj.insert_end(12)
    obj.insert_end(3)
    obj.insert_end(4)
    obj.insert_end(8)
    obj.insert_end(9)
    obj.insert_end(100)
    print('original linked')
    obj.print_list()
    obj.partition(7)



