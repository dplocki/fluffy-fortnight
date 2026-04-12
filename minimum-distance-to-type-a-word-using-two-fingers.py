class Solution:
    def minimumDistance(self, word: str) -> int:
        n = len(word)
        asci_a = ord('A')
        
        @cache
        def distance(from_letter, to_letter):
            if from_letter == None:
                return 0

            position1 = ord(from_letter) - asci_a
            position2 = ord(to_letter) - asci_a

            return abs(position1 // 6 - position2 // 6) + abs(position1 % 6 - position2 % 6)

        @cache
        def internal(index: int, finger1: int, finger2: int) -> int:
            if index == n:
                return 0
            
            move1 = distance(word[finger1] if finger1 != None else None, word[index]) + internal(index + 1, index, finger2)
            move2 = distance(word[finger2] if finger2 != None else None, word[index]) + internal(index + 1, finger1, index)

            return min(move1, move2)
        
        return internal(0, None, None)
