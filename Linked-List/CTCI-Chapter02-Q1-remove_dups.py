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

    def remove_dups(self):
        '''
        :return: none

        Logic:

        1) use Dictionary for identifying duplicate elements
        2) when found remove the element

        Time complexity: O(n) and Space: O(n)

        -------
        Alternative method:
        1) for every node lement iterate through entire linked list to find duplicate
        2) and then delete

        Time complexity: O(n * n),  No additional space is used

        '''



        dic = {}

        #edge case: where Linked list has no nodes or single node return none
        if self.head == None or self.head.next == None:
            print('less than 1 nodes so no dups')
            return

        node = self.head

        while(node):

            if node.data not in dic:
                #insert node.data into dictionary
                dic[node.data] = 1

                #previous node track is kept so to remove node
                prev = node
                node = node.next

            else:
                #when node is repeated, remove it
                dic[node.data] += 1
                prev.next = node.next
                node = node.next




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




if __name__=='__main__':
    obj = SLL()

    #driver code to populate list
    obj.insert_first(2)
    obj.insert_end(0)
    obj.insert_first(2)
    obj.insert_end(1)
    obj.insert_end(1)
    obj.insert_end(1)
    obj.insert_end(0)
    obj.insert_end(0)
    obj.insert_end(0)
    obj.insert_first(1)
    obj.insert_first(2)
    obj.insert_first(2)
    print('original list')
    obj.print_list()
    obj.remove_dups()
    print('After removing duplicates')
    obj.print_list()
