
front = 0
rear  = 0
mymax = 5
def isEmpty(queue):
    return len(queue) == 0

def enqueue(queue, item):
    queue.append(item)

def dequeue(queue):
    if (isEmpty(queue)):
        return "Deletion not possible because queue is empty"
    else:
        item = queue[0]
        del queue[0]
        return item

#Driver code
queue = []
ch = 0
while ch !=4:
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Display")
    print("4.Quit")
    ch = int(input("Enter choice(1 to 4):"))
    
    if ch == 1:
        if rear<mymax:
            item = input("Enter item:")
            enqueue(queue, item)
            rear = rear + 1
        else:
            print("Queue is full")
        
    elif ch == 2:
        if front == rear:
            print("Queue is empty")
        else:
            print(dequeue(queue))
            front = front + 1
            
    elif ch == 3:
        print(queue)
    else:
        break