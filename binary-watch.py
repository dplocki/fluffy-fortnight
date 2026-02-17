class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        return list(map(lambda t: f"{t[0]}:{t[1]:02}",
            self.find_all_hours(turnedOn, self.build_bits_cache())))

    def find_all_hours(self, turnedOn: int, bits: Dict[int, List[int]]) -> Generator[Tuple[int, int], None, None]:
        for bit_for_hour in range(turnedOn + 1):
            for hour in bits.get(bit_for_hour, ()):
                if hour >= 12:
                    continue

                for minutes in bits.get(turnedOn - bit_for_hour, ()):
                    yield hour, minutes

    def build_bits_cache(self) -> Dict[int, List[int]]:
        bits = {}

        for i in range(0, 60):
            i_bits = self.count_set_bits(i)
            if i_bits not in bits:
                bits[i_bits] = []

            bits[i_bits].append(i)

        return bits

    def count_set_bits(self, n: int) -> int:
        result = 0
        while n:
            n &= n - 1
            result += 1

        return result
