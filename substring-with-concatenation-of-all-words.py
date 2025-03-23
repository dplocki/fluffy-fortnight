class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        string_len = len(s)
        whole_substrings = len(words) * word_len
        result = []

        words_as_hash = {}
        for word in words:
            words_as_hash[word] = words_as_hash.get(word, 1)

        for index in range(string_len - whole_substrings + 1):
            curent_words_as_hash = words_as_hash.copy()

            for sub_words_index in range(word_len):
                start = index + word_len * sub_words_index
                sub_word = s[start:start + word_len]

                if curent_words_as_hash.get(sub_word, 0) > 0:
                    curent_words_as_hash[sub_word] -= 1
                else:
                    break

            if not any(curent_words_as_hash.values()):
                result.append(index)

        return result
