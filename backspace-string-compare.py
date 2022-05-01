from itertools import pairwise
def backspaceCompare(s, t):
    def type(input, backspaceChar):
        buffer = []
        for i in input:
            if i != backspaceChar:
                buffer.append(i)
            elif len(buffer) > 0:
                buffer.pop()
        return buffer
    return type(s, "#") == type(t, "#")
# Runtime: 64 ms, faster than 7.96% of Python3 online submissions for Backspace String Compare.
# Memory Usage: 13.8 MB, less than 98.80% of Python3 online submissions for Backspace String Compare.

s = "ab#c"
t = "ad#c"
print(backspaceCompare(s, t)) # True
s = "ab##"
t = "c#d#"
print(backspaceCompare(s, t)) # True
s = "a#c"
t = "b"
print(backspaceCompare(s, t)) # False
s = "a##c"
t = "#a#c"
print(backspaceCompare(s, t)) # True
s = "xywrrmp"
t = "xywrrmu#p"
print(backspaceCompare(s, t)) # True
s = "y#fo##f"
t = "y#f#o##f"
print(backspaceCompare(s, t)) # True
