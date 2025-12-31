class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        result = 0
        unsorted_pairs = set(range(n - 1))
        
        for col_idx in range(len(strs[0])):
            has_inversion = any(
                strs[index][col_idx] > strs[index + 1][col_idx]
                for index in unsorted_pairs)

            if has_inversion:
                result += 1
            else:
                unsorted_pairs = set(index
                    for index in unsorted_pairs
                    if strs[index][col_idx] == strs[index + 1][col_idx])

                if not unsorted_pairs:
                    break
        
        return result
