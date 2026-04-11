class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        result, current_gas = 0, 0
        gas_sum, cost_sum = 0, 0

        for index, (g, c) in enumerate(zip(gas, cost)):
            gas_sum += g
            cost_sum += c
            current_gas += g - c 
            if current_gas < 0:
                current_gas = 0
                result = index + 1

        if gas_sum < cost_sum:
            return -1

        return result
