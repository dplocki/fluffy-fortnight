class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return list(self.generate_lexical_order_numbers(n))

    def generate_lexical_order_numbers(self, n):
        current_value = 1
        for _ in range(n):
            yield current_value

            if current_value * 10 <= n:
                current_value *= 10
            else:
                while current_value % 10 == 9 or current_value + 1 > n:
                    current_value //= 10

                current_value += 1
