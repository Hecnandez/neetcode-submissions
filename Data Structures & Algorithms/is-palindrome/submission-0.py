class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join([char for char in s if char.isalnum()]).lower()
        print("cleaned: ", cleaned)
        print("reversed: ", cleaned[::-1])
        return cleaned == cleaned[::-1]
        