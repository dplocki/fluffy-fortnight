class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        s = iter(s)

        for d in takewhile(lambda d: d == '1', s):
            pass

        for d in s:
            if d == '1':
                return False
        
        return True
