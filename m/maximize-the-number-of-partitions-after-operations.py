class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        chars = [ord(letter) - ord('a') for letter in s]

        @cache
        def interal(index: int, current_mask: int, change_used: bool) -> int:
            if index == n:
                return 1

            result = 0
            current_char = chars[index]
            new_mask = current_mask | (1 << current_char)
            distinct_count = bin(new_mask).count('1')
            
            if distinct_count <= k:
                result = interal(index + 1, new_mask, change_used)
            else:
                result = 1 + interal(index + 1, 1 << current_char, change_used)
            
            if change_used:
                return result

            for new_char in range(26):
                new_mask_with_change = current_mask | (1 << new_char)
                distinct_count_with_change = bin(new_mask_with_change).count('1')
                
                if distinct_count_with_change <= k:
                    result = max(result, interal(index + 1, new_mask_with_change, True))
                else:
                    result = max(result, 1 + interal(index + 1, 1 << new_char, True))

            return result
        
        return interal(0, 0, False)
