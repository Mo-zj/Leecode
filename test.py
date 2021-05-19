class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = {}
        i, L = 0, 0
        n = len(s)
        if n < 1:
            return L

        for j in range(n):
            if s[j] in st.keys():
                # the last time the char appears is after the start index,
                # thus update the start idx
                if st[s[j]] > i:
                    i = st[s[j]]
            L = max(L, j - i + 1)
            st[s[j]] = j + 1

        return L


if __name__ == '__main__':

    so =  Solution()
    s = "abcabcbb"
    result = so.lengthOfLongestSubstring(s)
    print(result)
