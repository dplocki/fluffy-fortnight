class Solution:
    def isNumber(self, s: str) -> bool:
        return bool(re.match(r'^(-|\+)?((\d+\.\d*)|(\d+)|(\d*\.\d+))((e|E)(\+|-|)\d+)?$', s))
