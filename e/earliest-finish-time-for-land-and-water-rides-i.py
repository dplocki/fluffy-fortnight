class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        result = inf

        for land_id in range(len(landStartTime)):
            for water_id in range(len(waterStartTime)):
                land_start = landStartTime[land_id]
                land_duration = landDuration[land_id]
                water_start = waterStartTime[water_id]
                water_duration = waterDuration[water_id]

                result = min(result, max(land_start + land_duration, water_start) + water_duration)
                result = min(result, max(water_start + water_duration, land_start) + land_duration)

        return result
