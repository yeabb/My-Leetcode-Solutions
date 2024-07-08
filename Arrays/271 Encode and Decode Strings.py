class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """

        s = ""
        for word in strs:
            s += str(len(word)) + "#" + word
        return s
        
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        
        left = 0
        right = 0
        while s[right] != "#":
            right+=1
        
        output = []
        while right < len(s):
            length = int(s[left:right])
            output.append(s[right+1:right+length+1])
            left = right + length + 1
            right = left
            while right < len(s) and s[right] != "#":
                right += 1 

        return output


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))