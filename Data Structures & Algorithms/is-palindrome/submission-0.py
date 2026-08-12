class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new = ""
        for i in s:
            if i.isalnum():
                new += i

        left = 0
        right = len(new) - 1

        while left < right:
            if new[left] != new[right]:
                return False
            left +=1
            right -=1
        return True