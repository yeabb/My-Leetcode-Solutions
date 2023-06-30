from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordList.append(beginWord)

        #build the Adj list
        adj=defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern=word[:i] + "*" + word[i+1:]
                adj[pattern].append(word)
        
        q=deque()
        q.append(beginWord)
        visited=set()
        length=1
        while q:
            qLen=len(q)
            for i in range(qLen):
                word=q.popleft()
                if word==endWord:
                    return length
                visited.add(word)
                for i in range(len(word)):
                    pattern=word[:i] + "*" + word[i+1:]
                    for nbr in adj[pattern]:
                        if nbr != word and nbr not in visited:
                            q.append(nbr)
            length+=1
        
        return 0
        
                