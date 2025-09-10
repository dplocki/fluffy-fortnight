class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        languages = list(map(set, languages))
        maxium = 0
        person_know_language = defaultdict(int)
        person_know_language[0] = 0
        checked = set()

        def count_person(person_id: int) -> None:
            if person_id in checked:
                return

            checked.add(person_id)
            nonlocal maxium
            maxium += 1

            for language in languages[person_id - 1]:
                person_know_language[language] += 1

        for person_a, person_b in friendships:
            if languages[person_a - 1].isdisjoint(languages[person_b - 1]):
                count_person(person_a)
                count_person(person_b)

        return maxium - max(person_know_language.values())
