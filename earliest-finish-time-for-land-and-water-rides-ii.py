class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        result = inf

        def internal(start_time_1: List[int], duration_time_1: List[int], start_time_2: List[int], duration_time_2: List[int]):
            finish_time_1 = min(
                start_time_1[index] + duration_time_1[index]
                for index in range(len(start_time_1)))

            return min(
                max(finish_time_1, start_time_2[index]) + duration_time_2[index]
                for index in range(len(start_time_2)))

        return min(
            internal(landStartTime, landDuration, waterStartTime, waterDuration),
            internal(waterStartTime, waterDuration, landStartTime, landDuration)
        )
