def _binom_mul_capped(res: int, total: int, add: int, cap: int) -> Tuple[int, bool]:
    if add == 0 or total == 0:
        return res, False

    bigger, smaller = (total, add) if total > add else (add, total)
    for i in range(1, smaller + 1):
        res = res * (bigger + i) // i
        if res > cap:
            return res, True
    return res, False


def kth_permutation_with_repeats(letters: List[str], k: int) -> Generator[str, None, None]:
    counts = Counter(letters)
    unique_sorted = sorted(counts.keys())
    n = len(letters)

    for _ in range(n):
        for ch in unique_sorted:
            c = counts[ch]
            if c == 0:
                continue

            counts[ch] -= 1

            res, total, exceeded = 1, 0, False
            for other in unique_sorted:
                cc = counts[other]
                if cc == 0:
                    continue
                res, exceeded = _binom_mul_capped(res, total, cc, k)
                total += cc
                if exceeded:
                    break

            if exceeded or res > k:
                yield ch
                break
            else:
                k -= res
                counts[ch] += 1


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
