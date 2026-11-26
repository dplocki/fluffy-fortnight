class Solution:
    def canAliceWin(self, n: int) -> bool:
        alice_turn = True
        required = 10

        while True:
            if n < required:
                return not alice_turn

            n -= required
            required -= 1
            alice_turn = not alice_turn
