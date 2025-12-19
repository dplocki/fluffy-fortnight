class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        result = set([0, firstPerson])
        for _, meetings in groupby(sorted(meetings, key=operator.itemgetter(2)), operator.itemgetter(2)):
            connections = defaultdict(set)
            waiting = []

            for a, b, _ in meetings:
                if a in result or b in result:
                    result.add(a)
                    result.add(b)

                    waiting.append(a)
                    waiting.append(b)
                else:
                    connections[a].add(b)
                    connections[b].add(a)

            visited = set()
            while waiting:
                a = waiting.pop()
                if a in visited:
                    continue

                visited.add(a)

                for b in connections[a]:
                    waiting.append(b)
                    result |= connections[b]

        return list(result)
