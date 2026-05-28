class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = { '<': None }
        lengths = {}

        for index, word in enumerate(wordsContainer):
            tmp = trie

            for letter in reversed(word):
                if letter not in tmp:
                    tmp[letter] = { '<': tmp }

                tmp = tmp[letter]

            current_word_len = len(word)

            tmp['^'] = index
            while tmp != None:
                if '?' in tmp:
                    if current_word_len >= tmp['?']:
                        break
                    
                    tmp['?'] = current_word_len
                    tmp['='] = index
                else:
                    tmp['?'] = current_word_len
                    tmp['='] = index

                tmp = tmp['<']


        result = []
        for query in wordsQuery:
            tmp = trie

            for letter in reversed(query):
                if letter not in tmp:
                    break
                
                tmp = tmp[letter]

            result.append(tmp['='])

        return result
