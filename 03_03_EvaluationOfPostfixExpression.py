def evalRPN(tokens):
    stack=[]
    for op in tokens:
        if op == '+':
            a,b = stack.pop(),stack.pop()
            stack.append(b+a)
        elif op == '-':
            a,b = stack.pop(),stack.pop()
            stack.append(b-a)
        elif op == '*':
            a,b = stack.pop(),stack.pop()
            stack.append(b*a)
        elif op == '/':
            a,b = stack.pop(),stack.pop()
            stack.append(int(b / a))
        else:
            stack.append(int(op))
    return stack.pop()

#Driver code
tokens = ["10", "6", "9", "3","+", "-11","*", "/","*", "17","+", "5","+"]
print(evalRPN(tokens))