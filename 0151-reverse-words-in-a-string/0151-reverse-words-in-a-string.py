class Solution(object):
    def reverseWords(self, s):

        word=s.split()

        reverseword=word[::-1]

        reverseWords=' '.join(reverseword)

        return reverseWords

