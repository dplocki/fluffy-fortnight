class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_index, b_index = len(a) - 1, len(b) - 1 
        result = []
        results = {
            ('0', '0', '0'): ('0', '0'),
            ('0', '0', '1'): ('1', '0'),
            ('1', '0', '0'): ('1', '0'),
            ('1', '0', '1'): ('0', '1'),
            ('0', '1', '0'): ('1', '0'),
            ('0', '1', '1'): ('0', '1'),
            ('1', '1', '0'): ('0', '1'),
            ('1', '1', '1'): ('1', '1'),
        }

        carring = '0'

        while a_index >= 0 or b_index >= 0 or carring == '1':
            first = a[a_index] if a_index >= 0 else '0'
            second = b[b_index] if b_index >= 0 else '0'

            digit, carring = results[first, second, carring]
            result.append(digit)

            a_index -= 1
            b_index -= 1

        return ''.join(result[::-1])
