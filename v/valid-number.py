class Solution:
    IS_NUMBER = re.compile(r'^(-|\+)?((\d+\.\d*)|(\d+)|(\d*\.\d+))((e|E)(\+|-|)\d+)?$')

    def isNumber(self, s: str) -> bool:
        return bool(re.match(Solution.IS_NUMBER, s))
