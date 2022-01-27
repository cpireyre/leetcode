from typing import *
def longestCommonPrefix(strs: List[str]) -> str:
    ret = ""
    for c in enumerate(min(strs, key=len)):
        S = {s[c[0]] for s in strs}
        if len(S) == 1:
            ret += c[1]
        else:
            break
    return ret
