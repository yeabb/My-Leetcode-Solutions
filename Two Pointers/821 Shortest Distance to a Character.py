class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        
       
        indxs = [i for i in range(len(s)) if s[i] == c]
        print(indxs)
        p1, p2, p3 = indxs[0], 0, 0
        answer = [0] * len(s)
        while p2 < len(s):
            if p1 == p2:
                answer[p2] = 0
                if p3+1<len(indxs):
                    p1 = indxs[p3+1]
                    p3+=1
                pass
            if p3 == 0:
                answer[p2] = abs(p1-p2)
            else:
                answer[p2] = min(abs(p1-p2), abs(indxs[p3-1] - p2))
                
            p2+=1
            
        return answer