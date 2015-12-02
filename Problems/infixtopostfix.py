def infixtopostfix(infixstring):
    op_order ={"(":1,"+":2,"-":2,"*":3,"/":3}
    infixlist =infixstring.split()
    postfixlist =[]
    stack =[]
    for i in infixlist:
        if ( i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or i in"0123456789"):
            postfixlist.append(i)
        elif (i == "("):
            stack.append(i)
        elif( i == ")"):
            token = stack.pop()
            while (token != "("):
                postfixlist.append(token)
                token = stack.pop()
        else:
            while( len(stack) != 0) and (op_order[stack[len(stack)-1]] >= op_order[i]):
                    postfixlist.append(stack.pop())
            stack.append(i)
          
    while len(stack) != 0:
         postfixlist.append(stack.pop())
       
    return "".join(postfixlist)         
            
    