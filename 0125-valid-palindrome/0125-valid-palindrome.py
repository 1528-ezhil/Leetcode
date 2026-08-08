class Solution(object):
    def isPalindrome(self, s):
        new_s = ""

        for ch in s:
            if ch.isalnum():
                new_s += ch.lower()

        return new_s == new_s[::-1]