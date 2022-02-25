def compareVersions(version1, version2):
        parse = lambda ver: [int(s) for s in ver.split(".")]
        version1, version2 = parse(version1), parse(version2)
        lv1, lv2 = len(version1), len(version2)
        version1, version2 = version1 + [0]*(lv2 - lv1), version2 +[0]*(lv1 - lv2)
        for a, b in zip(version1, version2):
            if a > b:
                return 1
            elif a < b:
                return -1
        return 0
# Runtime: 38 ms, faster than 62.44% of Python3 online submissions for Compare Version Numbers.
# Memory Usage: 13.9 MB, less than 68.52% of Python3 online submissions for Compare Version Numbers.

version1 = "1.01"
version2 = "1.001"
print(compareVersions(version1, version2))
version1 = "1.0"
version2 = "1.0.0"
print(compareVersions(version1, version2))
version1 = "0.1"
version2 = "1.1"
print(compareVersions(version1, version2))
