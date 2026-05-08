def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        primes, imporant_points, n = {}, [], 0

        for index, num in enumerate(nums):
            n += 1
            if is_prime(num):
                primes[num] = []
                imporant_points.append(index)

        for index, num in enumerate(nums):
            for prime in primes:
                if num % prime == 0:
                    primes[prime].append(index)

        imporant_points.append(n - 1)
        to_check = [(0, 0)]
        result = {}

        while to_check:
            current_jumps, current_index = heapq.heappop(to_check)
            if current_jumps > n - 1:
                continue

            if current_index in result and result[current_index] < current_jumps:
                continue 

            result[current_index] = current_jumps
            if current_index == n - 1:
                return current_jumps
        
            if nums[current_index] in primes:
                new_jumps = current_jumps + 1
                for new_index in primes[nums[current_index]]:
                    if new_index not in result or result[new_index] > new_jumps:
                        heapq.heappush(to_check, (new_jumps, new_index))

            for new_index in imporant_points:
                if new_index == current_index:
                    continue

                new_jumps = current_jumps + abs(current_index - new_index)
                if new_jumps > n - 1:
                    continue
 
                if new_index not in result or result[new_index] > new_jumps:
                    heapq.heappush(to_check, (new_jumps, new_index))
