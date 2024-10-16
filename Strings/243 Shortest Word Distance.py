class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        

        index1, index2 = -1, -1
        output = len(wordsDict)

        for i in range (len(wordsDict)):
            if wordsDict[i] == word1:
                index1 = i
            elif wordsDict[i] == word2:
                index2 = i

            if index1 != -1 and index2 != -1:
                output = min(output, abs(index1-index2))

        return output


