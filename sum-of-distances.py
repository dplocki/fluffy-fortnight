class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        indexes = defaultdict(list)
        for index, value in enumerate(nums):
            indexes[value].append(index)
      
        result = [0] * len(nums)
        for indices in indexes.values():
            index_count = len(indices)
            left_sum = 0
            right_sum = sum(indices) - index_count * indices[0]
          
            for i in range(index_count):
                result[indices[i]] = left_sum + right_sum
              
                if i + 1 >= index_count:
                    continue

                gap = indices[i + 1] - indices[i]
                left_sum += gap * (i + 1)
                right_sum -= gap * (index_count - i - 1)
    
        return result
