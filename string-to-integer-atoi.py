class Solution:
    def myAtoi(self, s: str) -> int:
        sign = None
        digits = []       
   
        begin_string = True
        for character in s:
            if character == ' ' and begin_string:
                pass
            elif character == '-' and begin_string:
                if sign != None:
                    return 0

                begin_string = False
                sign = -1
            elif character == '+' and begin_string:
                if sign != None:
                    return 0

                begin_string = False
                sign = 1
            elif character == '0':
                begin_string = False
                digits.append(0)
            elif character == '1':
                begin_string = False
                digits.append(1)
            elif character == '2':
                begin_string = False
                digits.append(2)
            elif character == '3':
                begin_string = False
                digits.append(3)
            elif character == '4':
                begin_string = False
                digits.append(4)
            elif character == '5':
                begin_string = False
                digits.append(5)
            elif character == '6':
                begin_string = False
                digits.append(6)
            elif character == '7':
                begin_string = False
                digits.append(7)
            elif character == '8':
                begin_string = False
                digits.append(8)
            elif character == '9':
                begin_string = False
                digits.append(9)
            elif begin_string:
                return 0
            else:
                break

        sign = sign or 1
        multiplayer = len(digits) -1
        result = 0

        for digit in digits:
            result += 10 ** multiplayer * digit
            multiplayer -= 1

        if result > (2**31 - 1):
            return sign * (2**31 - 1) if sign == 1 else -2**31

        return sign * result
