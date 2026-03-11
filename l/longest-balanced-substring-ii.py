class Solution:
    def longestBalanced(self, s: str) -> int:
        states = [(0, 0, 0)]
        for letter in s:
            last = states[-1]
            states.append((
                last[0] + (1 if letter == 'a' else 0),
                last[1] + (1 if letter == 'b' else 0),
                last[2] + (1 if letter == 'c' else 0)))

        result = 0
        first_occurence = {}
        for index, (a, b, c) in enumerate(states):
            for key in (
                ("abc", a - b, a - c),
                ("ab", a - b, c),
                ("bc", b - c, a),
                ("ca", c - a, b),
                ("a", b, c),
                ("b", c, a),
                ("c", a, b),
            ):
                result = max(result, index - first_occurence.get(key, index))
                first_occurence.setdefault(key, index)

        return result
