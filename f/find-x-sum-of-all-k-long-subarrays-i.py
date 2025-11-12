class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        freq = Counter(nums[:k])
        result = [self.calculate_x_sum_from_freq(freq, x)]

        for i in range(k, len(nums)):
            freq[nums[i]] += 1

            left = nums[i - k]
            freq[left] -= 1

            result.append(self.calculate_x_sum_from_freq(freq, x))

        return result
    
    def calculate_x_sum_from_freq(self, freq: dict, x: int) -> int:
        sorted_items = sorted(freq.items(), key=lambda item: (-item[1], -item[0]))
        x_sum = sum(value * count for value, count in sorted_items[:x])
        return x_sum
