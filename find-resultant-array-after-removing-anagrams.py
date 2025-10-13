class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        prev = None
        result = []

        for word in words:
            tmp = Counter(word)
            if prev != tmp:
                result.append(word)
                prev = tmp

        return result
