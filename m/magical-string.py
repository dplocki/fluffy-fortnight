class Solution:
    def magicalString(self, n: int) -> int:
        magical_str = [1, 2, 2]
        index = 2  
        while len(magical_str) < n:
            last_value = magical_str[-1]
            current_value = 3 - last_value
            magical_str.extend([current_value] * magical_str[index])
            index += 1

        return magical_str[:n].count(1)
