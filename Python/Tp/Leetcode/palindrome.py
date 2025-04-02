class Solution(object):
    def isPalindrome(self, x):
        if len(str(x)) == 1:
            return True
        str_x = str(x)
        for i in range(len(str_x)//2):
            if str_x[i] != str_x[-1-i]:
                return False
        return True


response = Solution().isPalindrome(1000021)
print(response)