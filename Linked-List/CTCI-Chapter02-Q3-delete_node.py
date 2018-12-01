'''
Problem Statement: Delete middle node
In this implementation I have implemented an alogorithm to delete any given node (be it 1st, middle or last)

TIme complexity: 
'''


class Node:
    def __init__(self,data):
        self.data = data     #intialize data
        self.next = None     #default next pointer is set to none


class SLL:

    #initialize head with None
    def __init__(self):
        self.head = None
        self.count = 0

    def print_list(self):
        temp = self.head

        while(temp != None):
            print(temp.data, end='--->')
            temp = temp.next


    def insert_first(self,data):
        self.count += 1
        node = Node(data)


        if self.head == None:
            self.head = node
            return

        node.next = self.head
        self.head = node


    def insert_end(self,data):
        self.count += 1

        node = Node(data)

        if self.head == None:
            self.head = node
            return

        else:
            temp = self.head
            while (temp.next != None):
                temp = temp.next
            temp.next = node

    def remove_node(self,val):
        '''
        
        :param val: value of node that is to be deleted
        :return: nothing
        '''
        p = self.head
        
        
        #edge case: Linked list has no nodes
        if (self.head == None):
            print('LL has no nodes')
            return None
        
        #prev pointer maintained so that node with data == val can be removed
        prev = self.head
        
        while(p):
            #if head is to be removed
            if (p.data == val and p == self.head):
                self.head = self.head.next
                
            #for all other nodes excluding head
            elif(p.data == val):
                prev.next = p.next
                
            prev = p
            p = p.next

if __name__=='__main__':
    obj = SLL()
    
    #populate linked list
    obj.insert_first(1)
    obj.insert_end(2)
    obj.insert_end(3)
    obj.insert_end(4)
    obj.insert_end(5)
    obj.insert_end(6)
    #obj.insert_end(7)
    #obj.insert_end(8)
    #obj.insert_end(9)
    #obj.insert_end(10)
    #obj.insert_end(11)
    #obj.insert_end(12)
    obj.print_list()

    #print(obj.count)

    #obj.kth_to_last(4)
    obj.remove_node(5)
    obj.remove_node(1)
    obj.remove_node(2)
    obj.remove_node(3)
    obj.remove_node(4)
    obj.remove_node(6)
    print('after')
    obj.print_list()


