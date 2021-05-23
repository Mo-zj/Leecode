"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

 
示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0
 
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        flag = 0
        # flag = 1
        re = 0
        li = []

        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        for i in range(len(s)):
            j = i+1
            for k in range(j, len(s)):
                if s[i] == s[k]:
                    flag = k - i + 1
                    break
                else:
                    flag = k - i
                    # flag += 1

                    if s[k] in s[i:k]:
                        re += 1
                    print("flag=" + str(flag))
                    print("re=" + str(re))
                    flag = flag - re



            li.append(flag)
            for i in range(len(li)):
                print("li"+str(i)+"="+str(li[i]))
            # flag = 0
            flag = 0
            re = 0

        max = 0
        for i in range(len(li)-1):
            if li[i] > li[i + 1]:
                now = li[i]
            else:
                now = li[i + 1]

            if now > max:
                max = now

        return max


if __name__ == '__main__':

    so =  Solution()
    s ="pwwkew"
    result = so.lengthOfLongestSubstring(s)
    print(result)





