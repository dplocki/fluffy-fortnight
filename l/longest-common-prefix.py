class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''

        for w in zip_longest(*strs, fillvalue=None):
            letters = {*w}
            if None in letters or len(letters) > 1:
                break

            result += tuple(letters)[0]

        return result
