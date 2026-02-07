class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        current_number = 1        

        for num in target:
            while current_number < num:
                result.append('Push')
                result.append('Pop')
                current_number += 1

            result.append('Push')
            current_number += 1

        return result
