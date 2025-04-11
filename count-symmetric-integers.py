class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result = 0
        current = low
        while current <= high:
            if current < 10:
                current = 10
                continue

            if 10 <= current < 100:
                if current % 11 == 0:
                    result += 1

                current += 1
                continue
                
            if 100 <= current < 1000:
                current = 1000
                continue

            if 1000 <= current < 10000:
                d1 = current // 1000
                d2 = (current // 100) % 10
                d3 = (current // 10) % 10
                d4 = current % 10

                if d1 + d2 == d3 + d4:
                    result += 1

                current += 1

        return result
