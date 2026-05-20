class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen = set()
        result = []
        count_common = 0

        for a, b in zip(A, B):
            if a in seen:
                count_common += 1
            else:
                seen.add(a)
            
            if b in seen:
                count_common += 1
            else:
                seen.add(b)

            result.append(count_common)

        return result
