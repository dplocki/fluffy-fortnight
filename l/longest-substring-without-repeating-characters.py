class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters_inside_window = set()
        left, result = 0, 0

        for right, letter in enumerate(s):
            while letter in letters_inside_window:
                letters_inside_window.remove(s[left])
                left += 1

            letters_inside_window.add(letter)
            result = max(result, right - left + 1)

        return result
