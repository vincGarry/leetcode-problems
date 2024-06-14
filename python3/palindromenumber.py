class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :return False
    
        reverse_num = 0
        temp = x

        while temp != 0:
            num = temp % 10
            reverse_num = reverse_num * 10 + num
            temp //= 10

        return reverse_num == x