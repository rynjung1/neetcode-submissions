class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # dictionary wit keys as unique letter_count tuple & values as strings

        for str in strs: 
            letter_count = [0] * 26 # creates list where every 0 represents frequency of a letter in alphabet

            for char in str:
                letter_count[ord(char) - ord('a')] += 1 # finds the 0 attributted to the current char and increments
            
            result[tuple(letter_count)].append(str) # appends the str to the corresponding tuple of letter_count (or creates new key-value pair)

        return list(result.values()) # returns only the values (the corresponding str's are grouped bc anagrams are under same key)