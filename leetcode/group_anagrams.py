

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}
        for str in strs:
            key = ''.join(sorted(str))
            if str_dict.get(key, None) == None:
                str_dict[key] = [str]
            else:
                values = str_dict.get(key)
                values.append(str)
        anagrams = list(str_dict.values())
        anagrams = sorted(anagrams, key=lambda x: len(x))

        answers = []
        for anagram in anagrams:
            answers.append(sorted(anagram))

        return answers

strs = ["eat","tea","tan","ate","nat","bat"]
#strs = [""]
#strs = ["a"]
print(Solution().groupAnagrams(strs))
