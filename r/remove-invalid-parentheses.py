class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        def internal() -> Generator[str, None, None]:
            stack = [(s, 0, 0, ("(", ")"))]

            while stack:
                sub_s, start, border, pair = stack.pop()
                balance = 0
                match = False

                for index in range(start, len(sub_s)):
                    balance += (sub_s[index] == pair[0]) - (sub_s[index] == pair[1])
                    if balance >= 0:
                        continue

                    for cursor in range(border, index + 1):
                        if sub_s[cursor] != pair[1] or (cursor != border and sub_s[cursor - 1] == pair[1]):
                            continue

                        stack.append((sub_s[:cursor] + sub_s[cursor + 1 :], index, cursor, pair))

                    match = True
                    break

                if match:
                    continue

                new_sub_s = sub_s[::-1]
                if pair[0] == "(":
                    stack.append((new_sub_s, 0, 0, (")", "(")))
                else:
                    yield new_sub_s


        return list(internal())
