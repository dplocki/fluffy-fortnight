class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        sorted_letters = ''.join(sorted(s))
        if sorted_letters[::-1] == target:
            return ''

        used_letters = [False] * n
        result = []

        def internal(position: int, cannot_be_lesser: bool):
            if position == n:
                return ''.join(result) > target

            for i, v in enumerate(used_letters):
                if v:
                    continue

                if cannot_be_lesser and sorted_letters[i] < target[position]:
                    continue

                used_letters[i] = True
                result.append(sorted_letters[i])

                if internal(position + 1, cannot_be_lesser and sorted_letters[i] <= target[position]):
                    return True

                result.pop()
                used_letters[i] = False

            return False

        internal(0, True)
        return ''.join(result)
