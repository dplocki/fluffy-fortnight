class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        word1_len, word2_len = len(word1), len(word2)
        last = [-1] * word2_len
        index2 = word2_len - 1
        for index1 in range(word1_len - 1, -1, -1):
            if index2 >= 0 and word1[index1] == word2[index2]:
                last[index2] = index1
                index2 -= 1
        
        result, skip, index2 = [], 0, 0
        for index1, letter in enumerate(word1):
            if index2 == word2_len:
                break

            if letter == word2[index2] or skip == 0 and (index2 == word2_len - 1 or index1 < last[index2 + 1]):
                skip += letter != word2[index2]
                result.append(index1)
                index2 += 1
        
        if index2 == word2_len:
            return result
        
        return []
