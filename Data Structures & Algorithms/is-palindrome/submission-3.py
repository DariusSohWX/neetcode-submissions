class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_s = s.replace(" ", "").lower()
        i = 0
        j = len(new_s) - 1

        while i < j:
            while i < j and not new_s[i].isalnum():
                i += 1

            while i < j and not new_s[j].isalnum():
                j -= 1

            if i < j and new_s[i] != new_s[j]:
                return False

            i += 1
            j -= 1

        return True