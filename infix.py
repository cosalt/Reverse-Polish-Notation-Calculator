def infix(string):
    stack = [" " for i in range(len(string))]
    topofstack = -1
    arr = string.split()
    temp = []
    for i in arr:
        if i in ["*", "+", "-", "/"]:
            temp.append(i)
        else:
            topofstack += 1
            stack[topofstack] = i
            if len(temp) != 0:
                topofstack += 1
                stack[topofstack] = temp[0]
                temp.pop()
    return stack
