class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = ""
        for a, b, c in zip(num, num[1:], num[2:]):
            if a == b == c and a > result:
                result = a

        return result * 3
