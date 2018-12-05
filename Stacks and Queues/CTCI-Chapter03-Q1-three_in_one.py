'''
Problem Statement: Using single array to implement 3 stacks


Method1: implement list with a fixed size and divide the list in fixed size
Disadvantage: Memory is not used efficiently

Method2: All stacks is dynamic
Logic: maintained 2 arrays
1st array -- to store elements of stack
2nd array -- stores current position where next element is to be inserted

lets say we have 3 stacks s1,s2,s3 and elements in them are example: [s1e1: element 1 of stack 1, s2e1: element 1 of stack 2 ...]
way of storing elements in 1st array [s1e1,s2e1,s3e1,s1e2,s2e2,s3e3 and so on ...]
'''


class multipleStacks():
    def __init__(self,k):
        #intialize array and current list
        self.array = [None] * k
        self.current = [x for x in range(k)]
        self.k = k

    def push(self,element,stackno):
        if stackno not in [0,1,2]:
            print('invalid stack number')
            return None
        else:

            if (self.current[stackno] >= len(self.array)):
                self.array += [None] * self.k
                print('increased',self.array)

            #pushing elements in array
            self.array[self.current[stackno]] = element

            #increament current array position to point to correct one
            self.current[stackno] += 3
            print('push',self.array,self.current)

    def pop(self,stackno):
        if stackno not in [0,1,2]:
            print('invalid stack number')
            return None
        else:
            if(self.current[stackno] < self.k):
                print('no element in stack',stackno)
            else:
                #1st decrement current so that correct element can be popped
                self.current[stackno] -= 3
                print('pop',self.array[self.current[stackno]])
                self.array[self.current[stackno]] = 0
                print(self.array,self.current)


    def top(self,stackno):
        if stackno not in [0,1,2]:
            print('invalid stack number')
            return None
        elif(self.current[stackno] < self.k):
            print('no element in stack',stackno)
        else:
            print(self.array[self.current[stackno]-3])


def main():
    obj = multipleStacks(3)

    obj.push(3,5)
    obj.push(4, 1)
    obj.push(5,2)

    obj.push(6, 0)
    obj.push(7, 1)

    obj.pop(4)
    obj.pop(2)
    #obj.pop(2)

    obj.top(2)



main()


