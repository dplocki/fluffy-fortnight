class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        result, current_depth = [], 0

        for letter in seq:
            if letter == "(":
                current_depth += 1
                result.append(current_depth % 2)
            else:
                result.append(current_depth % 2)
                current_depth -= 1

        return result
