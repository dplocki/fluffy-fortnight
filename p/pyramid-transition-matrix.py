class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        possible_tops = {}
        for left_base, right_base, top in allowed:
            base = (left_base, right_base)
            if base not in possible_tops:
                possible_tops[base] = set()

            possible_tops[base].add(top)

        @cache
        def internal(bottom: str) -> bool:
            if len(bottom) == 2:
                return (bottom[0], bottom[1]) in possible_tops

            possibles = []
            for base in pairwise(bottom):
                if base not in possible_tops:
                    return False
                
                possibles.append(possible_tops[base])

            return any(
                internal(''.join(raw_bottom))
                for raw_bottom in product(*possibles)
            )

        return internal(bottom)
