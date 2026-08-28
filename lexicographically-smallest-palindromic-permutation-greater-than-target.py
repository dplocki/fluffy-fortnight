class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        frequencies = defaultdict(int)

        for letter in s:
            frequencies[letter] += 1

        middle_letter = ''
        for letter, count in frequencies.items():
            if count % 2 == 0:
                frequencies[letter] //= 2
                continue

            if middle_letter:
                return '' # palindrome cannot be build (there can be only one 'middle' letter)

            middle_letter = letter
            frequencies[letter] = (frequencies[letter] - 1) >> 1

        palindrome_size = n // 2
        palindrome = []

        def internal(position: int, cannot_be_lesser: bool) -> str:
            if position == palindrome_size:
                first_part = ''.join(palindrome)
                result = first_part + middle_letter + first_part[::-1]

                if result > target:
                    return result
                
                return ''

            for letter in string.ascii_lowercase:
                if frequencies[letter] == 0:
                    continue

                if cannot_be_lesser and letter < target[position]:
                    continue

                how_much_letter = 1 if cannot_be_lesser else frequencies[letter]
                palindrome.extend(letter * how_much_letter)
                frequencies[letter] -= how_much_letter

                result = internal(position + how_much_letter, cannot_be_lesser and letter <= target[position])
                if result:
                    return result

                del palindrome[-how_much_letter:]
                frequencies[letter] += how_much_letter

            return ''


        return internal(0, True)
