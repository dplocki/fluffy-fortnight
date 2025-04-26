class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]
        for i in range(len(encoded)):
            result.append(encoded[i] ^ result[i])

        return result
