class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        connections_map = self.build_connection_map(wordList + [beginWord])
        parents_map = self.find_paths(connections_map, beginWord, endWord)
        return self.build_paths(parents_map, beginWord, endWord)

    def build_connection_map(self, word_list):
        connections = defaultdict(set)
        for word_a, word_b in combinations(word_list, 2):
            if self.differ_by_one_char(word_a, word_b):
                connections[word_a].add(word_b)
                connections[word_b].add(word_a)
        return connections

    def build_paths(self, parents_map, begin_word: str, end_word: str):
        def backtrack(word):
            if word == begin_word:
                return [(begin_word,)]
            
            paths = []
            for parent in parents_map[word]:
                for path in backtrack(parent):
                    paths.append((*path, word))
            
            return paths
        
        return backtrack(end_word)

    def find_paths(self, connections: Dict[str, Set], begin_word: str, end_word: str):
        current_level = {begin_word}
        visited = {begin_word}
        parents = defaultdict(set)

        while current_level and end_word not in current_level:
            next_level = set()
            level_visited = set()

            for current_word in current_level:
                for next_word in connections[current_word]:
                    if next_word not in visited and next_word not in level_visited:
                        next_level.add(next_word)
                        level_visited.add(next_word)
                    
                    if next_word not in visited:
                        parents[next_word].add(current_word)
            
            visited.update(level_visited)
            current_level = next_level

        return parents

    def differ_by_one_char(self, word1: str, word2: str):
        return sum(c1 != c2 for c1, c2 in zip(word1, word2)) == 1
