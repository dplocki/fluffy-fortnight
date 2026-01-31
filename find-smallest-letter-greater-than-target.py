class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for letter in sorted(letters):
            if letter > target:
                return letter
        
        return letters[0]
