class Solution:
    VOWELS = set('aAeEiIoOuU')

    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        wordlist = wordlist[::-1]
        words_lower = {
            word.lower(): word
            for word in wordlist
        }
        words_devowel = {
            self.devowel(word): word 
            for word in wordlist
        }
        wordlist = set(wordlist)

        results = []
        for word in queries:
            if word in wordlist:
                results.append(word)
                continue 
            
            word_lower = word.lower()
            if word_lower in words_lower:
                results.append(words_lower[word_lower])
                continue

            word_devowel = self.devowel(word)
            if word_devowel in words_devowel:
                results.append(words_devowel[word_devowel])
                continue

            results.append('')
                
        return results

    def devowel(self, word: str) -> str:
        return tuple(
            '_' if letter in Solution.VOWELS else letter
            for letter in word.lower()
        )
