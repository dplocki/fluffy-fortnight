@cache
def is_prime(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True


def prime_factors_generator(num: int) -> Generator[int, None, None]:
    p = 2
    factors = []
    while p * p <= num:
        if num % p == 0:
            yield p
            while num % p == 0:
                num //= p
        p += 1

    if num > 1:
        yield num


@cache
def prime_factors(num: int) -> Tuple[int]:
    return tuple(prime_factors_generator(num))


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        primes = defaultdict(list)
        imporant_points, n = [], 0

        for index, num in enumerate(nums):
            n += 1
            for prime in prime_factors(num):
                primes[prime].append(index)

        to_check = deque([(0, 0)])
        visited = set()
        visited.add(0)

        while to_check:
            current_jumps, current_index = to_check.popleft()
            if current_index == n - 1:
                return current_jumps

            for new_index in (current_index - 1, current_index + 1):
                if 0 <= new_index < n and new_index not in visited:
                    visited.add(new_index)
                    to_check.append((current_jumps + 1, new_index))

            if is_prime(nums[current_index]):
                for prime in prime_factors(nums[current_index]):
                    while primes[prime]:
                        new_index = primes[prime].pop()
                        if new_index not in visited:
                            visited.add(new_index)
                            to_check.append((current_jumps + 1, new_index)) 
