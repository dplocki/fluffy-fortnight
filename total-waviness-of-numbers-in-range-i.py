class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        result = 0

        for num in range(num1, num2 + 1):
            iterator = iter(self.get_digits(num))
            window = deque(islice(iterator, 2), maxlen=3)
            for x in iterator:
                window.append(x)
                if window[0] < window[1] > window[2]:
                    result += 1
                elif window[0] > window[1] < window[2]:
                    result += 1
            
        return result

    def get_digits(self, num: int) -> Generator[int, None, None]:
        while num:
            yield num % 10
            num //= 10
