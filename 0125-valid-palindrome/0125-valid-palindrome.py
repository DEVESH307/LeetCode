# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         clean = ''.join(c.lower() for c in s if c.isalnum())
#         return clean[::] == clean[::-1]


class Solution:
    def checkPalindrome(self, arr, i, j):
        if i >= j:
            return True

        if arr[i] != arr[j]:
            return False
        
        return self.checkPalindrome(arr, i+1, j-1)


    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(c.lower() for c in s if c.isalnum())
        i = 0
        j = len(clean)-1
        return self.checkPalindrome(clean, i, j)
        