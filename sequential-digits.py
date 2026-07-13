class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        str_low = str(low)
        length = len(str_low)
        first_digit = int(str_low[0])
        result = []

        while True:
            if first_digit + length > 10:
                length += 1
                first_digit = 1

            if length > 9:
                break

            sequence = digit = first_digit
            for _ in range(length - 1):
                digit += 1
                sequence *= 10
                sequence += digit

            if sequence > high:
                break

            if sequence >= low:
                result.append(sequence)

            first_digit += 1

        return result
