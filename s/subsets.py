class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return list(self.get_permutations(nums))

    def get_permutations(self, nums: List[int]):
        for permutation in range(2 ** len(nums)):
            yield tuple(self.get_permutation(nums, permutation))
    
    def get_permutation(self, nums: List[int], permutation: int):
            index = 0
            while permutation:
                if permutation % 2 == 1:
                    yield nums[index]

                permutation //= 2
                index += 1
