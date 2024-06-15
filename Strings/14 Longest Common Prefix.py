class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        strs = sorted(strs)
        common = ""

        for i in range(0, min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] != strs[-1][i]:
                return common
            common+= strs[0][i]
        return common

#Runtime = O(nlogn + 200) 
#        = O(1)