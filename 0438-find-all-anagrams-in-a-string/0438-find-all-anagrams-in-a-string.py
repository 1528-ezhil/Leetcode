from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Finds all start indices of p's anagrams in s.
        
        Time Complexity: O(N) where N = len(s)
        Space Complexity: O(1) since character set is limited to 26 lowercase letters
        """
        len_p, len_s = len(p), len(s)
        if len_p > len_s:
            return []

        p_count = Counter(p)
        s_count = Counter()
        result = []

        for i in range(len_s):
            # Add current character to window
            s_count[s[i]] += 1

            # Remove character that slid out of the window
            if i >= len_p:
                left_char = s[i - len_p]
                if s_count[left_char] == 1:
                    del s_count[left_char]
                else:
                    s_count[left_char] -= 1

            # Check if current window matches p's frequencies
            if s_count == p_count:
                result.append(i - len_p + 1)

        return result