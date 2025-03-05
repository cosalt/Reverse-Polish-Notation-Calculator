def rpn(arr):
    stack = [" " for i in range(len(arr))]
    topofstack = -1
    for count, number in enumerate(arr):
        if number in ["*", "+", "-", "/"]:
            num1 = str(stack[topofstack])
            topofstack -= 1
            num2 = str(stack[topofstack])
            topofstack -= 1
            sum = eval(num2 + number + num1)
            topofstack += 1
            stack[topofstack] = sum
        else:
            topofstack += 1
            stack[topofstack] = number
    return stack[topofstack]
