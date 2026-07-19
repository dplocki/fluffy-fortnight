class Solution:
    def smallestSubsequence(self, s: str) -> str:
        letters = {}
        for letter in s:
            letters[letter] = letters.get(letter, 0) + 1

        result = []
        current_letters = set()
        for letter in s:
            if letter not in current_letters:
                while result and result[-1] > letter:
                    if letters[result[-1]] > 0:
                        current_letters.remove(result[-1])
                        result.pop()
                    else:
                        break
                current_letters.add(letter)
                result.append(letter)
            letters[letter] -= 1

        return ''.join(result)
