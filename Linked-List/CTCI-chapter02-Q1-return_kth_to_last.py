'''
Problem Statement: implement an algorithm to find kth element to last

explantation: 3rd element to last means: last lement: 1st --> last second: 2nd --> element before --> 3rd (return this one)
example: Linked list:  1 --> 2 --> 3 --> 4 --> 5 --> 6 --> 7 --> 8 --> 9 --> 10 --> 11 --> 12
K = 4  {element retruned here is 8}


Solution:
Method 1: using 2 pointer method (Pointers p and q)
steps:
1) intialize pointer q at kth node
2) initialize pointer p at head
3) till q pointer reaches last node: traverse both p and q pointers
4) now q pointer is at last node while p is at kth element


Method 2:
we can keep a count of nodes when populating linked list, and then just traverse to kth node

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

    def kth_to_last(self,k):
        '''

        :param k: position k
        :return: kth node data
        '''
        count = 0
        end1 = self.head   
        start = self.head
        
        #intialize pointer end1 to kth node
        while(count < k):
            count += 1
            #print(count, end1.data)

            if end1 != None:
                end1 = end1.next

            else:
                print('Linked list has less than',k,' elements')
                return
        #print(count)

        #traverse: end pointer to last node, start pointer to kth node
        while(end1 != None):
            end1 = end1.next

            start = start.next

        return(start.data)





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




if __name__=='__main__':
    obj = SLL()
    
    #populate linked list
    obj.insert_first(1)
    obj.insert_end(2)
    obj.insert_end(3)
    obj.insert_end(4)
    obj.insert_end(5)
    obj.insert_end(6)
    obj.insert_end(7)
    obj.insert_end(8)
    obj.insert_end(9)
    obj.insert_end(10)
    obj.insert_end(11)
    obj.insert_end(12)


    print('linked list')
    obj.print_list()

    
    element = obj.kth_to_last(12)
    print(element)


