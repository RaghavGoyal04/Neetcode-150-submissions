class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagrams = defaultdict(list)
        # for s in strs:
        #     anagrams[tuple(sorted(s))].append(s)
        # return [val for val in anagrams.values()]

        anagrams = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
            anagrams[tuple(count)].append(s)
        return [val for val in anagrams.values()]
        