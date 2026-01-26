class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result = []
        minimum_distance = float('inf')

        for i in range(len(arr) - 1):   
            distance = arr[i + 1] - arr[i]
            if distance < minimum_distance:
                result = []
                minimum_distance = distance

            if distance == minimum_distance:
                result.append((arr[i], arr[i + 1]))

        return result
