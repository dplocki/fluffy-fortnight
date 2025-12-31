class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        all_apples = sum(apple)

        for index, cap in enumerate(accumulate(sorted(capacity, reverse=True)), 1):
            if cap >= all_apples:
                return index
