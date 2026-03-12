from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            groups[key].append(s)
        return list(groups.values())
if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(['abc', 'bca', 'tta', 'att']))

