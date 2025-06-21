class Solution:
    def __init__(self):
        self.factorials_cache = { 1: 1, 2: 2, 3: 6 }

    def getPermutation(self, n: int, k: int) -> str:
        return ''.join(map(str, self.get_permutation(list(range(1, n + 1)), k - 1)))

    def get_permutation(self, elements, k):
        n = len(elements)
        if n == 1:
            yield elements[0]
            return
   
        first_element_cycle = self.factorial(n - 1)
        first_element_index = k // first_element_cycle
        first_element = elements[first_element_index]

        yield first_element
        yield from self.get_permutation(
            [element for element in elements if element != first_element],
            k % first_element_cycle)

    def factorial(self, n):
        if n in self.factorials_cache:
            return self.factorials_cache[n]

        result = n * self.factorial(n - 1)
        self.factorials_cache[n] = result
        return result
