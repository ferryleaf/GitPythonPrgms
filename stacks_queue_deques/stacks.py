'''
Create Basic Stack & it's functionalities

STACK: LIFO[LAST-IN-FAST-OUT]
FUNCTIONALITY:
    1.  PUSH
    2.  POP
    3.  IS_EMPTY
    4.  LENGTH
    5.  TOP

'''

class Empty(Exception):
    pass

class stack:
    def __init__(self):
        self.__list=[]

    def push(self,val):
        self.__list.append(val)

    def pop(self):
        if not self.is_empty():
            self.__list.pop()
        else:
            raise Empty("Stack is Empty.")

    def top(self):
        if not self.is_empty():
            return self.__list[-1]
        else:
            raise Empty("Stack is Empty.")

    def is_empty(self):
        return (self.__len__()==0)

    def __len__(self):
        return len(self.__list)

    def display(self):
        return self.__list


if __name__=='__main__':
    s=stack()
    print(s.is_empty())
    s.push(5)
    s.push(6)
    s.push(7)
    print(s.__len__())
    print(s.display())
    print(s.top())
    s.pop()
    print(s.display())
    s.pop()
    s.pop()
    print(s.display())
    s.pop()
