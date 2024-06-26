class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        arr = []
        tracker = dic[s[0]]

        for i in range(1, len(s)):
            if dic[s[i]] < dic[s[i-1]]:
                arr.append(tracker)
                tracker = dic[s[i]]
            elif dic[s[i]] == dic[s[i-1]]:
                tracker+=dic[s[i]]                       
            else:
                tracker = dic[s[i]] - dic[s[i-1]]

        arr.append(tracker)
        return sum(arr)

