class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a_numbers, b_numbers = set(), set()
        common_count = 0
        result = []

        for a, b in zip(A, B):
            a_numbers.add(a)
            b_numbers.add(b)

            result.append(len(a_numbers & b_numbers))
    
        return result
