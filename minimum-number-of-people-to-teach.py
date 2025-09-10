class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        language_knowing = {
            person: set(know_languages)
            for person, know_languages in enumerate(languages, start=1)
        }

        friendship_pair = [(a, b) for a, b in friendships if not language_knowing[a] & language_knowing[b]]

        result = 999
        for language in range(1, n + 1):
            local_result = set()
            for a, b in friendship_pair:
                if language not in language_knowing[a]:
                    local_result.add(a)

                if language not in language_knowing[b]:
                    local_result.add(b)

            result = min(result, len(local_result))

        return result
