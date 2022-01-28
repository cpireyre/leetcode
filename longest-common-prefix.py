from typing import *
def longestCommonPrefix(strs: List[str]) -> str:
    ret = ""
    for c in enumerate(strs[0]):
        for s in strs[1:]:
            if s[c[0]] != c[1]:
                return ret
        ret += c[1]
    return ret
