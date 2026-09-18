class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first, last = {}, {}
        for index, character in enumerate(s):
            first.setdefault(character, index)
            last[character] = index

        intervals = []
        for character in first:
            l, r = first[character], last[character]
            lo = hi = l
            while lo > l or hi <= r:
                if lo > l:
                    lo -= 1
                    c = s[lo]
                else:
                    c = s[hi]
                    hi += 1

                l = min(l, first[c])
                r = max(r, last[c])

            intervals.append((l, r))

        intervals.sort(key=lambda p: (p[1], -p[0]))
        result = []
        prev_end = -1
        for l, r in intervals:
            if l <= prev_end:
                continue

            result.append(s[l:r + 1])
            prev_end = r

        return result
