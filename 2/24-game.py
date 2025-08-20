class Solution:
    OPERATIONS = [operator.add, operator.sub, operator.mul]

    def judgePoint24(self, cards: List[int]) -> bool:
        return any(map(self.is_hand_gives_24, permutations(cards)))

    def is_hand_gives_24(self, hand: List[int]):

        def is_24(value: float) -> bool:
            return abs(value - 24.0) < 1e-6

        def internal(source_a, source_b):
            for a, b in product(source_a, source_b):
                for operation in Solution.OPERATIONS:
                    yield operation(a, b)

                if b != 0:
                    yield a / b

        if any(map(is_24, internal(
            internal((hand[0],), (hand[1],)),
            internal((hand[2],), (hand[3],))
        ))):
            return True

        if any(map(is_24, internal((hand[0],), internal((hand[1],), internal((hand[2],), (hand[3],)))))):
            return True

        return False
