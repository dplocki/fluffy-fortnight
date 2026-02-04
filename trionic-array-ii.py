class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)

        def build_phase_array(operator: Callable[[int, int], bool]) -> Dict[int, Tuple[int, int]]:
            start, current_sum = None, 0
            for index in range(1, n):
                if operator(nums[index - 1], nums[index]):
                    if start == None:
                        start = index - 1

                    current_sum += nums[index]
                elif start != None:
                    yield start, index - 1, current_sum
                    current_sum = 0
                    start = None

            if start != None:
                yield start, n - 1, current_sum

        def internal(increasing: Dict[int, Tuple[int, int]], decreasing: Dict[int, Tuple[int, int]]) -> Generator[int, None, None]:
            for array1_start, (array1_end, array1_value) in increasing.items():
                if array1_end not in decreasing:
                    continue

                array2_end, array2_value = decreasing[array1_end]
                if array2_end not in increasing:
                    continue

                current_sum = nums[array1_start] + array1_value + array2_value

                for index in range(array2_end, increasing[array2_end][0]):
                    current_sum += nums[index + 1]
                    yield current_sum

        increasing = {}
        for start, end, value in build_phase_array(operator.lt):
            for index in range(start, end):
                increasing[index] = (end, value)
                value -= nums[index + 1]

        decreasing = { start: (end, value) for start, end, value in build_phase_array(operator.gt) }

        return max(internal(increasing, decreasing))
