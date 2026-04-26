class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        return list(filter(lambda q: any(self.is_hamming_distance_below_2(q, d) for d in dictionary), queries))
    
    def is_hamming_distance_below_2(self, source: str, target: str):
        distance = 0
        for s, t in zip(source, target):
            if s != t:
                distance += 1
            
            if distance > 2:
                return False

        return True
