class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        to_check = deque([(beginWord, 1)])

        while to_check:
            word, transformation_count = to_check.popleft()

            if word == endWord:
                return transformation_count

            for i in range(len(word)):
                for c in ascii_lowercase:
                    new_word = word[:i] + c + word[i + 1:]
                    if new_word in words:
                        to_check.append((new_word, transformation_count + 1))
                        words.remove(new_word)

        return 0

        
