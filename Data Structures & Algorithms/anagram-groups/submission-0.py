class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for ele in strs:
            key = [0] * 26
            for char in ele:
                key[ord(char) - ord("a")] += 1

            groups[tuple(key)].append(ele)

        return list(groups.values())