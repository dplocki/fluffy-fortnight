class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strip_right = s.rstrip()
        return len(strip_right) - strip_right.rfind(' ') - 1
