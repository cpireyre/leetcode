class Solution:
    def judgeCircle(self, moves: str) -> bool:
        m = Counter(moves)
        return m['U'] == m['D'] and m['L'] == m['R']
#Runtime: 44 ms, faster than 88.95% of Python3 online submissions for Robot Return to Origin.
#Memory Usage: 14.1 MB, less than 98.03% of Python3 online submissions for Robot Return to Origin.
