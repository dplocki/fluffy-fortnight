class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        lefts, rights, empties = 0, 0, 0
        for move in moves:
            if move == 'L':
                lefts += 1
            elif move == 'R':
                rights += 1
            else:
                empties += 1

        return max(lefts, rights) - min(lefts, rights) + empties
