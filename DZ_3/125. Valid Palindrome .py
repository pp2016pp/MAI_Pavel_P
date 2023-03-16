class Solution:
    def isPalindrome(self, text: str) -> bool:
        text = text.casefold()
        #text = text.replace(' ', '')

        for j in text:
            if j.isalnum() == False:
                text = text.replace(j,'')

        for i in range(len(text)):
            if text[i] != text[(len(text)-1-i)]:
                return False

        return True


    
# https://leetcode.com/problems/valid-palindrome/