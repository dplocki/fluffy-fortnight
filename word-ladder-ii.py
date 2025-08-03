class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        connections_map = self.build_connection_map(wordList + [beginWord])
        paths = list(self.find_paths(connections_map, beginWord, endWord))
        return paths

    def build_connection_map(self, wordList):
        connections = defaultdict(set)
        for word_a, word_b in combinations(wordList, 2):
            if self.differ_by_one_char(word_a, word_b):
                connections[word_a].add(word_b)
                connections[word_b].add(word_a)
        return connections

    def find_paths(self, connections: Dict[str, Set], beginWord: str, endWord: str):
        to_check = deque([(beginWord,)])
        path_min = 500
        visited = set()

        while to_check:
            path = to_check.popleft()
            path_size = len(path)
            last_path = path[-1]

            if path_size > path_min:
                continue

            if last_path == endWord:
                if path_min > path_size:
                    path_min = path_size

                yield path
                continue

            for neighbor in connections[last_path]:
                if neighbor not in visited:
                    to_check.append((*path, neighbor))

            visited.add(last_path)

    def differ_by_one_char(self, word1: str, word2: str):
        return sum(c1 != c2 for c1, c2 in zip(word1, word2)) == 1
