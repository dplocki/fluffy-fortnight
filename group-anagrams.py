class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for single_str in strs:
            result[''.join(sorted(single_str))].append(single_str)

        return list(result.values())
