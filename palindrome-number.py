class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_as_str = str(x)
        return x_as_str == x_as_str[::-1]
