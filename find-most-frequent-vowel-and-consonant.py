class Solution:
    VOWELS = set('aeiou')

    def maxFreqSum(self, s: str) -> int:
        result_vowel = 0
        result_consonat = 0
        letters = defaultdict(int)

        for letter in s:
            letters[letter] += 1

            if letter in Solution.VOWELS:
                result_vowel = max(result_vowel, letters[letter])
            else:
                result_consonat = max(result_consonat, letters[letter])

        return result_vowel + result_consonat
