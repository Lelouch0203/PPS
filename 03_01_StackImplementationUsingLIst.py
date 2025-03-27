def create_stack():
    stack = []
    return stack
def isEmpty(stack):
    return stack == []
def push(stack,item):
    stack.append(item)
def pop(stack):
    if len(stack) > 0:
        item=stack.pop()
        return item
    else:
        return "\nStack Empty....\n"
stack = create_stack()
while True:
    print("1.Push")
    print("2.Pops")
    print("3.Display")
    print("4.Quit")
    ch = int(input("Enter choice:"))
    
    if ch == 1:
        item = int(input("Enter data:"))
        push(stack,item)
        
    elif ch == 2:
        if isEmpty(stack):
            print("Stack is empty")
        else:
            print("Popped item", pop(stack))
            
    elif ch == 3:
        print(stack)
        
    else:
        break