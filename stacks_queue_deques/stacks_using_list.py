'''
Create Basic Stack & it's functionalities

STACK: LIFO[LAST-IN-FRIST-OUT]
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
        return ("Pushed",  val)

    def pop(self):
        if not self.is_empty():
            num = self.__list.pop(self.__len__() - 1)
            return ("Pop ", num)
        else:
            return ("Stack is Empty.")

    def top(self):
        if not self.is_empty():
            return self.__list[-1]
        else:
            return ("Stack is Empty.")

    def is_empty(self):
        return (self.__len__()==0)

    def __len__(self):
        return len(self.__list)

    def display(self):
        return self.__list


if __name__=='__main__':
    s=stack()
    print("size", s.__len__())
    print("isEmpty", s.is_empty())
    print("pop", s.pop())
    print("top", s.top())
    print("push", s.push(5))
    print("top", s.top())
    print("size", s.__len__())
    print("isEmpty", s.is_empty())
    print("display", s.display())
    print("push", s.push(51))
    print("push", s.push(45))
    print("push", s.push(5))
    print("push", s.push(6))
    print("push", s.push(7))
    print("display", s.display())
    print("size", s.__len__())
    print("isEmpty", s.is_empty())
    print("pop", s.pop())
    print("top", s.top())
    print("display", s.display())
