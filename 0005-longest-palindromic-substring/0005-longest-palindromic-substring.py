class Solution:
    def expend(self, s, left, right):
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1

        return left+1, right-1

        
    def longestPalindrome(self, s: str) -> str:
        start = end = 0

        for i in range(len(s)):
            # odd length Palindrome
            l1, r1 = self.expend(s, i, i)
            if r1-l1 > end-start:
                start, end = l1, r1

            # even length Palindrome
            l2, r2 = self.expend(s, i, i+1) 
            if r2-l2 > end-start:
                start, end = l2, r2

        return s[start:end+1]
        