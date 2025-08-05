class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        last_character = None
        last_character_count = 0

        for c in s:
            if last_character == c:
                last_character_count += 1
            else:
                last_character_count = 0

            last_character = c

            if last_character_count < 2:
                result.append(c)

        return ''.join(result)
