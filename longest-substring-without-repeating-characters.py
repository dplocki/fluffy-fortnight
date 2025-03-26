class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0

        letters_inside_window = set()
        maximum_right = len(s)
        left, right = -1, 0
        result = 1

        while True:
            while right < maximum_right:
                letter = s[right]

                if letter in letters_inside_window:
                    result = max(result, len(letters_inside_window))
                    left += 1
                    letter = s[left]
                    letters_inside_window.remove(letter)
                else:
                    letters_inside_window.add(letter)
                    result = max(result, len(letters_inside_window))
                    right += 1

            if right == maximum_right:
                return result
