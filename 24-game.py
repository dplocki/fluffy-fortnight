class Solution:
    OPERATIONS = [operator.add, operator.sub, operator.mul, operator.truediv, operator.sub, lambda a, b: b - a]

    def judgePoint24(self, cards: List[int]) -> bool:
        for hand in permutations(cards):
            if self.is_hand_gives_24(hand):
                return True

        return False

    def is_hand_gives_24(self, hand: List[int]):
        def internal(index: int, current_result):
            if index == 4:
                return abs(current_result - 24.0) < 1e-6

            for operation in Solution.OPERATIONS:
                if internal(index + 1, operation(current_result, hand[index])):
                    return True

            if current_result != 0 and internal(index + 1, hand[index] / current_result):
                return True

            return False

        return internal(1, hand[0])
