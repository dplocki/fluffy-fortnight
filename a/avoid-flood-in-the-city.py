class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        result = []
        sunny_days = []
        history = {}

        for day, lake in enumerate(rains):
            if lake > 0:
                if lake in history:
                    result_index = next((d for d in sunny_days if d > history[lake]), None)
                    if result_index == None:
                        return []

                    result[result_index] = lake
                    sunny_days.remove(result_index)
                history[lake] = day
                result.append(-1)
            else:
                sunny_days.append(day)
                result.append(1)         

        return result
