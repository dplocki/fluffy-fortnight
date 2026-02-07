class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        n_target = len(target)
        target_index = 0

        for i in range(1, n + 1): 
            result.append('Push')
            if i == target[target_index]:
                target_index += 1
                if target_index >= n_target:
                    break
            else:
                result.append('Pop')

        return result
