class Solution:
    def minInsertions(self, s: str) -> int:
        result, brackets_counter, index = 0, 0, 0
        length = len(s)

        while index < length:
            if s[index] == '(':
                brackets_counter += 1
            else:
                if brackets_counter > 0:
                    brackets_counter -= 1
                else:
                    result += 1
                
                if index < length - 1 and s[index + 1] == ')':
                    index += 1
                else:
                    result += 1

            index += 1

        return result + brackets_counter * 2
