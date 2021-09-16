
COUNT = 100

class Stack:
    def __init__(self, value):
        self.value = value;
        self.next = None



def test():
    top = None
    for i in range(0, COUNT):
        curr = Stack(f'Hello #{i}')
        curr.next = top
        top = curr
    print(stackSize(top))

def stackSize(stack):
    size = 0
    if stack is not None:
        size = stackSize(stack.next) + 1
    return size

if __name__ == "__main__":
    test()
