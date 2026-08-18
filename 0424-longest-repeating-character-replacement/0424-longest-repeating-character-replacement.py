class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_freq = 0
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            # Expand the window by including s[right]
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])
            
            # Shrink the window if replacements needed exceed k
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            
            # Record the maximum valid window size found
            max_len = max(max_len, right - left + 1)
            
        return max_len