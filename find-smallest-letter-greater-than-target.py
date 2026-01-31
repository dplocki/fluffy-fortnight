class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        result = 0
        left, right = 0, len(letters) - 1

        while left <= right:
            mid = (left + right) >> 1

            if letters[mid] > target:
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        if result == -1:
            return letters[0]
        
        return letters[result]
