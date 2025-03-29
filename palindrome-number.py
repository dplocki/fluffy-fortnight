class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_as_str = str(x)
        length = len(x_as_str)
        middle = length // 2

        for n in range(middle):
            if x_as_str[n] != x_as_str[length - n - 1]:
                return False

        return True
