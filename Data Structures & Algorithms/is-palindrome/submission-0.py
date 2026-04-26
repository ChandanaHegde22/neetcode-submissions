class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        res = s[::-1]
        if res == s:
            return True
        else:
            return False
        