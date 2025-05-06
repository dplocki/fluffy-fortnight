class Solution:
    digits_to_letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []

        results = ['']
        for digit in digits:
            new_result = []
            for result in results:
                for letter in Solution.digits_to_letters[digit]:
                    new_result.append(result + letter)

            results = new_result

        return results
