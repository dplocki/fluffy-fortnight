class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        result = s
        for key, value in knowledge:
            result = result.replace(f'({key})', value)

        return re.sub(r'\([a-z]+\)', '?', result)
