from collections import defaultdict
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

#The total number of recursive calls in the worst case would be O(3^m * 4^n), where m is the number of digits that map to 3 letters and n is the number of digits that map to 4 letters.------------------------------------------


        def mapNumToLetter():
            dic=defaultdict()
            string="abcdefghijklmnopqrstuvwxyz"
            left=0
            right=2
            for i in range(2,10):
                if i==7 or i==9:
                    dic[str(i)]=string[left:right+2]
                    right+=4
                    left+=4
                else:
                    dic[str(i)]=string[left:right+1]
                    left+=3
                    right+=3
            return dic


        def backTracking(indx):
    
            if indx==len(digits):
                string="".join(tempList)
                if string:
                    res.append(string)
                return


            for i in range(len(dic[digits[indx]])):
                tempList.append(dic[digits[indx]][i])
                backTracking(indx+1)
                tempList.pop()
        

        dic=mapNumToLetter()
        res, tempList = [], []
        backTracking(0)
        return res
        