class Solution:
    def grayCode(self, n: int) -> List[int]:
        current = [0]

        for multiplayer in range(n):
            addition = 2 ** multiplayer

            new_current = current[:]
            
            for c in reversed(current):
                new_current.append(addition + c)
            
            current = new_current
        
        return current
