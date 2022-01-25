from itertools import dropwhile, takewhile

# List comprehensions can't work because
# they don't guarantee an insertion order, or something.
#def validMountainArray(arr):
#    if (len(arr) < 3) or not (arr[0] < arr[1]):
#        return False
#
#    peak = max(arr)
#    back = [x for x in arr if arr.index(x) > arr.index(peak) and x < peak]
#    print(back)
#    front = [x for x in arr if arr.index(x) < arr.index(peak) and x < peak]
#    print(front)
#    return arr == front + [peak] + back

def validMountainArray(arr):

    l = len(arr)
    if l < 3 or not (arr[0] < arr[1]):
        return False

    i = 1
    while i < l and arr[i - 1] < arr[i]:
        i += 1
    if i == l:
        return False
    while i < l and arr[i - 1] > arr[i]:
        i += 1
    return i == l


def runTests(f, T):
    for t in T:
        print(t[0])
        if f(t[0]) != t[1]:
            print("KO")
            return
        else:
            print("OK")

testCases = [([2,1], False), ([3,5,5], False), ([0,3,2,1], True),
        ([0,2,3,4,6,2,1,0], True), ([0,2,3,3,5,2,1,0], False),
        ([0,1,2,3,4,5,6,7,8,9], False)]
runTests(validMountainArray, testCases)
