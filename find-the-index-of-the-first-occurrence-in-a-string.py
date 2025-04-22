class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for index in range(len(haystack) - len(needle) + 1):
            if haystack[index] == needle[0] and self.check_substring(index, haystack, needle):
                return index

        return -1

    def check_substring(self, start: int, haystack: str, needle: str):
        for j in range(1, len(needle)):
            if haystack[start + j] != needle[j]:
                return False

        return True
