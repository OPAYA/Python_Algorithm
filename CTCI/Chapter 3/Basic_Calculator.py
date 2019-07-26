def Calcul(s):
	op_stack, val_stack, i = [], [], len(s) - 1
	op_map = {"+": lambda x, y: x + y, "-": lambda x, y: x - y}
	while i >= 0:
	    j = i - 1
	    print('j', 'i', j, i)
	    print(s[i])
	    if s[i].isdigit():
	        while j >= 0 and s[j].isdigit():
	            j -= 1
	        val_stack.append(int(s[j+1:i+1]))
	        print('val', val_stack)
	    elif s[i] in {"+", "-", ")"}:
	        op_stack.append(s[i])
	        print('op', op_stack)
	    elif s[i] == "(":
	        while op_stack[-1] != ")":
	            op, x, y = op_stack.pop(), val_stack.pop(), val_stack.pop()
	            val_stack.append(op_map[op](x, y))
	        op_stack.pop()
	    i = j
	while op_stack:
	    x, y = val_stack.pop(), val_stack.pop()
	    val_stack.append(op_map[op_stack.pop()](x, y))
	return val_stack[0]

print(Calcul('(1+(3+4)-3)'))