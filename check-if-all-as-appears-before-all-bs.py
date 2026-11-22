class Solution:
    def checkString(self, s: str) -> bool:
        a_phase = True
        for letter in s:
            if letter == 'a':
                if not a_phase:
                    return False
            else:
                a_phase = False

        return True
