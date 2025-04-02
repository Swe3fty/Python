class Solution(object):
    def longestCommonPrefix(self, strs):
        prefixe = ""
        for i in range(len(strs)):
            if i+1 < len(strs) and strs[i][i] == strs[i+1][i]:
                prefixe += strs[i][i]
        return prefixe



strs1 = ["dog","racecar","car"]
strs2 = ["flower","flow","flight"]     

response = Solution().longestCommonPrefix(strs2)
print(response)