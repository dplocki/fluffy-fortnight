class Solution:
    def simplifyPath(self, path: str) -> str:
        result = []
        for token in path.split('/'):
            if not token:
                continue
            elif token == '.':
                continue
            elif token == '..':
                if result:
                    result.pop()
            else:
                result.append(token)

        return '/' + '/'.join(result)
