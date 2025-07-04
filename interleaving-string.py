class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        max_s1, max_s2, max_s3 = len(s1), len(s2), len(s3)
        if max_s1 + max_s2 != max_s3:
            return False

        propositions = deque([(0, 0)])
        while propositions:
            first, second = propositions.popleft()

            if first + second == max_s3:
                return True

            if first < max_s1 and s1[first] == s3[first + second]:
                propositions.append((first + 1, second))

            if second < max_s2 and s2[second] == s3[first + second]:
                propositions.append((first, second + 1))
        
        return False
