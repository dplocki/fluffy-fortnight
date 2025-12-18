class Solution:
    COUPON_PATTERN = re.compile(r'[a-zA-Z0-9_]+')

    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        result = {
            'electronics': [],
            'grocery': [],
            'pharmacy': [],
            'restaurant': [],
        }

        for index, identifier in enumerate(code):
            if not isActive[index]:
                continue

            if businessLine[index] not in result:
                continue

            if Solution.COUPON_PATTERN.fullmatch(identifier) == None:
                continue

            result[businessLine[index]].append(identifier)

        return list(chain.from_iterable(
            sorted(result[value])
            for value in result.keys()))
