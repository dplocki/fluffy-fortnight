class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        secret_know_day = { 0: 1 }

        for _ in range(n):
            new_secret_know_day = { 0: 0 }

            for day, people in secret_know_day.items():
                if day >= forget:
                    continue

                new_secret_know_day[day + 1] = people
                if day >= delay:
                    new_secret_know_day[1] += people

            secret_know_day = new_secret_know_day

        return sum(secret_know_day.values()) % (10**9 + 7)
