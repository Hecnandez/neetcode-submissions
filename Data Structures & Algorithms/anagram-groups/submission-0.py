class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        k = 0
        anagrams = []
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in hashmap:
                anagrams[hashmap[sorted_word]].append(word)
            else:
                hashmap[sorted_word] = k
                anagrams.append([word])
                k += 1
        return anagrams
