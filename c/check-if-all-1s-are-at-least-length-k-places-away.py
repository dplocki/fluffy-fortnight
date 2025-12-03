class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        return all(
            map(
                lambda s: s >= k,
                map(
                    lambda s: s[1] - s[0] - 1,
                    pairwise(
                        map(
                            itemgetter(0),
                            filter(
                                lambda n: n[1] == 1,
                                enumerate(nums)))))))
