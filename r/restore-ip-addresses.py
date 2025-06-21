class Solution:

    def __init__(self):
        self.pattern = re.compile(r'^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$')

    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12 or s == '':
            return []

        return list(self.check('', s))

    def check(self, correct_prefix: str, leftovers: str):
        if correct_prefix.count('.') == 3:
            if self.is_ip_valid(correct_prefix + leftovers): 
                yield correct_prefix + leftovers
            return

        if leftovers == '':
            return

        yield from self.check(correct_prefix + leftovers[0], leftovers[1:])
        if correct_prefix == '' or correct_prefix[-1] == '.':
            return

        yield from self.check(correct_prefix + '.', leftovers)

    def is_ip_valid(self, ip):
        return all(
            bool(self.pattern.match(token))
            for token in ip.split('.', 4))
