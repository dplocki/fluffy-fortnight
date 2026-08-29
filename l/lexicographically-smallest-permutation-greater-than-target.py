class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        frequesies = defaultdict(int)

        for letter in s:
            frequesies[letter] += 1

        for letter in target:
            frequesies[letter] -= 1

        for index in range(len(target) - 1, -1, -1):
            frequesies[target[index]] += 1

            if any(x < 0 for x in frequesies.values()):
                continue

            next_letter = None
            for candidate in string.ascii_lowercase[ord(target[index]) - ord('a') + 1:]:
                if not frequesies[candidate]:
                    continue

                next_letter = candidate
                break

            if next_letter == None:
                continue

            frequesies[next_letter] -= 1

            result = list(target[:index])
            result.append(next_letter)

            for letter in string.ascii_lowercase:
                result.extend(letter * frequesies[letter])

            return ''.join(result)

        return ''
