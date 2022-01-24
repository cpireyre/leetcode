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

# 40 ( 41 )
# 91 [ 93 ]
# 123 { 125 }

# bytearray ver:
# Excellent memory profile but slower
#def isValid(s):
#    if (len(s) % 2):
#        return False
#    stack = [0]
#    for c in bytes(s, 'ascii'):
#        if (c == 40) | (c == 91) | (c == 123):
#            stack.append(c)
#        else:
#            p = stack.pop()
#            if not (((p == 40) & (c == 41))
#                    | ((p == 91) & (c == 93))
#                    | ((p == 123) & (c == 125))):
#                return False
#    return stack == [0]

# Sets ver, inspired by one of the Leetcode submissions:
#def isValid(s):
#    opens = {'(', '[', '{'}
#    pairs = {'()', '[]', '{}'}
#    stack = []
#    for c in s:
#        if c in opens:
#            stack.append(c)
#        elif not stack:
#            return False
#        elif stack.pop() + c not in pairs:
#            return False
#    return not stack
# Actually slower with worse memory usage

def runTests(f, T):
    for t in T:
        print(t[0])
        if f(t[0]) != t[1]:
            print("KO")
            return
        else:
            print("OK")
            
testCases = [('()', True), ("()[]{}", True), ("(]", False), ("((", False), ("[", False)]
runTests(isValid, testCases)
