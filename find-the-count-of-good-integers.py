class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        n_is_odd = n % 2 == 1
        seen = set()

        for digits in self.find_all_k_palindromic(n, k, n_is_odd):
            self.find_all_number(seen, digits, n, n_is_odd)

        return len(seen)

    def find_all_k_palindromic(self, n, k, n_is_odd):
        half_n = n // 2

        for first_digit in range(1, 10):
            if n > 1:
                for p in product(range(10), repeat=(half_n - (0 if n_is_odd else 1))):
                    digits = (first_digit, *p)
                    if self.find_good_integer(k, n_is_odd, (first_digit, *p)):
                        yield digits
            else:
                digits = (first_digit,)
                if self.find_good_integer(k, n_is_odd, digits):
                    yield digits

    def find_good_integer(self, k, n_is_odd, digits):
        n = len(digits) 
        result = 0
        number = 0
        multiplayer = 1
        for d in digits:
            number += multiplayer * d
            multiplayer *= 10

        for index in range(n - 2 if n_is_odd else n - 1, -1, -1):
            number += multiplayer * digits[index]
            multiplayer *= 10

        return number % k == 0

    def find_all_number(self, seen, digits, n, n_is_odd):
        mirror_part = digits[:-1] if n_is_odd else digits
        for p in permutations((*digits, *mirror_part)):
            if p[0] == 0 or p in seen:
                continue

            seen.add(p)
        
        return seen
