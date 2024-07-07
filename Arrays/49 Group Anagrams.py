class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = {}
        arr = [0] * 26
        for string in strs:
            for chr in string:
                arr[ord(chr)-97] += ord(chr)

            tup = tuple(arr)
            if tup in dic:
                dic[tup].append(string)
            else:
                dic[tup] = [string]
            arr = [0] * 26
        
        return list(dic.values())
