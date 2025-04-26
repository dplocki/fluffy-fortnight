class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]
        for item in encoded:
            result.append(result[-1] ^ item)

        return result
