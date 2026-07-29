def permutations_count(counts: Counter[str]) -> int:
    n = sum(counts.values())
    denom = 1

    for c in counts.values():
        denom *= factorial(c)

    return factorial(n) // denom


def kth_permutation_with_repeats(letters: List[str], k: int) -> Generator[str, None, None]:
    counts = Counter(letters)
    unique_sorted = sorted(counts.keys())
    n = len(letters)

    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i

    denom = 1
    for c in counts.values():
        denom *= fact[c]

    total = n

    for _ in range(n):
        for ch in unique_sorted:
            c = counts[ch]
            if c == 0:
                continue

            new_denom = denom // c
            remaining_after = total - 1
            block = fact[remaining_after] // new_denom

            if k < block:
                counts[ch] -= 1
                denom = new_denom
                total -= 1
                yield ch
                break
            else:
                k -= block


class Solution:        
    def smallestPalindrome(self, s: str, k: int) -> str:
        s_letters = Counter(s)

        middle = ''
        letters_to_permutation = []
        for l, c in s_letters.items():
            if c % 2 == 1:
                middle = l
                c -= 1

            if c == 0:
                continue

            letters_to_permutation += [l] * (c >> 1)

        if not letters_to_permutation:
            return middle

        letters_to_permutation.sort()
        letters_lenght = len(letters_to_permutation)

        result = ''.join(kth_permutation_with_repeats(letters_to_permutation, k - 1))

        if not result or len(result) != letters_lenght:
            return ''

        return result + middle + result[::-1]
