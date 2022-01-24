def isValid(s):
    if (len(s) % 2):
        return False
    stack = []
    for c in s:
        if c == '(' or c == '[' or c == '{':
            stack.append(c)
        else:
            if not(stack):
                return False
            o = stack.pop()
            if not((o == '(' and c == ')')
                    or (o == '[' and c == ']')
                    or (o == '{' and c == '}')):
                return False
    return not(stack)

def runTests(f, T):
    for t in T:
        print(t[0])
        if f(t[0]) != t[1]:
            print("KO")
            return
        else:
            print("OK")
            
testCases = [('()', True), ("()[]{}", True), ("(]", False)]
runTests(isValid, testCases)
