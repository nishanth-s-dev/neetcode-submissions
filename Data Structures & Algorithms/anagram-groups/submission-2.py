class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for string in strs:
            sorted_string = tuple(sorted(string))
            if sorted_string not in res:
                res[sorted_string] = [string]
            else:
                res[sorted_string].append(string)
        return res.values()