import fileinput

def rpn_1(infix):
    out = []
    stack = []

    for token in infix:
        if token.isnumeric():
            out.append(int(token))
        elif token in '*+':
            while stack and stack[-1] in '*+':
                out.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                out.append(stack.pop())
            stack.pop()

    while stack:
        out.append(stack.pop())
    
    return out

def rpn_2(infix):
    out = []
    stack = []

    for token in infix:
        if token.isnumeric():
            out.append(int(token))
        elif token == '*':
            while stack and stack[-1] in '*+':
                out.append(stack.pop())
            stack.append(token)
        elif token == '+':
            while stack and stack[-1] in '+':
                out.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                out.append(stack.pop())
            stack.pop()

    while stack:
        out.append(stack.pop())
    
    return out

def eval_rpn(postfix):
    out = []
    
    for token in postfix:
        if token == '+':
            out.append(out.pop() + out.pop())
        elif token == '*':
            out.append(out.pop() * out.pop())
        else:
            out.append(token)

    return out[0]

p1 = 0
p2 = 0
for line in fileinput.input():
    p1 += eval_rpn(rpn_1(line.strip()))
    p2 += eval_rpn(rpn_2(line.strip()))
print(p1)
print(p2)