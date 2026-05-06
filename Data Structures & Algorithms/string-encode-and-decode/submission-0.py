class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        # adds to the result string with format <wordlen>#<word>
        for s in strs: 
            result += str(len(s)) + "#" + s

        return result

    def decode(self, s: str) -> List[str]:
        result, i = [], 0

        while i < len(s):
            j = i

            while s[j] != "#": # scans until we hit #
                j += 1
            
            length = int(s[i : j]) # everything between i and j is the length of the current word

            result.append(s[j + 1 : j + 1 + length]) # skip past # and append the word to result 

            i = j + 1 + length # moves i to the start of the next word 
        
        return result

