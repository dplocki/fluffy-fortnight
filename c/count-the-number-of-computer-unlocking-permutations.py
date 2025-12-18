class Solution:
    MOD = 10**9 + 7

    def countPermutations(self, complexity: List[int]) -> int:
        computer_zero = complexity[0]
        for c in complexity[1:]:
            if c <= computer_zero:
                return 0

        return math.factorial(len(complexity) - 1) % Solution.MOD
