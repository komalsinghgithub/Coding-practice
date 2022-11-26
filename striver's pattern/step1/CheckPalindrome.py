
#Given an integer x, return true if x is a palindrome, and false otherwise.



class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)[::-1]
        if str(x)==y:
            return True
        else:
            return False    