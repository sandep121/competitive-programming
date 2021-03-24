from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        result = []
        updated_wordlist = [x.lower() for x in wordlist]
        repl={97: 95, 101: 95, 105: 95, 111: 95, 117: 95}
        vowel_less = [x.lower().translate(repl) for x in wordlist]
        for word in queries:
            if word in wordlist:
                result.append(word)
            elif word.lower() in updated_wordlist:
                result.append(wordlist[updated_wordlist.index(word.lower())])
            elif word.lower().translate(repl) in vowel_less:
                result.append(wordlist[vowel_less.index(word.lower().translate(repl))])
            else:
                result.append("")
        return result

print(Solution().spellchecker(["KiTe","kite","hare","Hare"],["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]))
