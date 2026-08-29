def is_t_correct(t: int) -> bool:
    divisibales = [0, 0, 0, 0]
    for index, divisible in enumerate((2, 3, 5, 7)):
        while t % divisible == 0:
            divisibales[index] += 1
            t //= divisible

    return t == 1


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        if not is_t_correct(t):
            return '-1'

        n = len(num)
        products = [0] * (n + 1)
        products[0] = t
        start_position = n - 1

        for index, digit in enumerate(num):
            if digit == '0':
                start_position = index
                break

            products[index + 1] = products[index] // math.gcd(products[index], int(digit))

        if products[-1] == 1:
            return num

        num_digits = list(num)
        for index in range(start_position, -1, -1):
            while True:
                num_digits[index] = chr(ord(num_digits[index]) + 1)
                if num_digits[index] > '9':
                    break

                current_t = products[index] // math.gcd(products[index], int(num_digits[index]))
                k = 9

                for j in range(n - 1, index, -1):
                    while current_t % k != 0:
                        k -= 1

                    current_t //= k
                    num_digits[j] = str(k)

                if current_t == 1:
                    return ''.join(num_digits)

        result = []
        original_t = t
        for digit in range(9, 1, -1):
            while original_t % digit == 0:
                result.append(str(digit))
                original_t //= digit

        result = ''.join(result)
        padding = max(n + 1 - len(result), 0)
        result += '1' * padding

        return result[::-1]
