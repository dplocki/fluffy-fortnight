class Solution:
    def maxOperations(self, s: str) -> int:
        s += '1'
        result = 0

        while True:
            i_index = s.find('10')
            if i_index == -1:
                return result

            r_index = s.find('01', i_index)
            if r_index == -1:
                return result

            result += 1
            s = s[:i_index] + '0' + s[i_index + 1:r_index] + '1' + s[r_index + 1:]

        return result
