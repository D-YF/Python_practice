class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        N = len(s)

        for i in range(N//2):
            left = i
            right = N-i-1
            temp = s[left]
            s[i] = s[right]
            s[right] = temp
        
        return s

## refine
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s)-1

        while left<right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp

            left += 1
            right -= 1
        
        return s

# s = ["h","e","l","l","o"]
# sol = Solution()
# print(sol.reverseString(s))

# O(N) and O(1)
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        left = 0
        right = left+k
        length = len(s)

        while left<=length:
            s = s[:left] + s[left:right][::-1] + s[right:]

            left += 2*k
            right += 2*k

        return s


# convert a string to a list
# O(N) and O(N)
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        left = 0
        right = left+k
        length = len(s)
        s = list(s)

        while left<=length:
            s[left:right] = s[left:right][::-1]

            left += 2*k
            right += 2*k

        return "".join(s)

# s = "abcdefg"
# k = 2
# sol = Solution()
# print(sol.reverseStr(s, k))


class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        N = len(s)

        for index, value in enumerate(s[::-1]):
            if value==" ":
                s = s[:N-index-1] + "%20" + s[N-index:]
        
        return s

# s = "We are happy."
# sol = Solution()
# print(sol.replaceSpace(s))

class Solution(object):
    def reverseStr(self, s):
        N = len(s)
        left, right = 0, N-1

        while left<right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp

            left += 1
            right -= 1
        
        return s
    

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        N = len(s)
        s = list(s)
        left, right = 0, N-1
        
        while s[left]==' ' or s[right]==' ':
            if s[left]==' ': 
                left += 1
            if s[right]==' ': 
                right -= 1
        s = s[left:right+1]

        s = self.reverseStr(s)
        N = len(s)
        
        new_s = []
        for i in range(N):
            if s[i]==' ':
                if new_s[-1] != ' ':
                    new_s.append(s[i])
                else:
                    continue
            else: 
                new_s.append(s[i])

        s = new_s
        N = len(s)
        left, right = 0, 0
        while right+1<=N:
            if right+1==N or s[right+1]==' ':
                s[left:right+1] = self.reverseStr(s[left:right+1])
                right += 2
                left = right
            else:
                right += 1

        return "".join(s)

# s = " the sky  is   blue  "
# sol = Solution()
# print(sol.reverseWords(s))


class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        return s[n:]+s[:n]

# s =  "lrloseumgh"
# k= 6
# sol = Solution()
# print(sol.reverseLeftWords(s, k))

class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        ans = ""
        N = len(s)

        for i in range(n, n+N):
            ans += s[i % N]
        return ans

# s = "abcdedf"
# k = 2
# sol = Solution()
# print(sol.reverseLeftWords(s, k))

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        N_needle = len(needle)
        N_haystack = len(haystack)

        for i in range(N_haystack):
            if haystack[i]==needle[0]:
                cur = 0
                while (i+cur)<N_haystack and cur<N_needle:
                    if haystack[i+cur]==needle[cur]:
                        cur += 1
                    else:
                        break
                if cur == N_needle:
                    return i
        return -1

# haystack = "leetcode"
# needle = "leeto"
# sol = Solution()
# print(sol.strStr(haystack, needle))


class Solution(object):
    def getLPSarray(self, pattern):
        N = len(pattern)
        length = 0

        LPS = [0]*N
        i = 1
        while i<N:
        ## e.g. aadaadaaf
            if pattern[i]==pattern[length]:
                length += 1
                LPS[i] = length
                i += 1
            else:
                if length == 0:
                    LPS[i] = 0
                    i += 1
                else:
                    ## This line is hard to understand
                    ## Step back to check new suffix
                    length = LPS[length-1]
        return LPS

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        N = len(haystack)
        M = len(needle)

        LPS = self.getLPSarray(needle)
        i, j = 0, 0

        while i <= N-(M-j):
            if haystack[i]==needle[j]:
                i += 1
                j += 1
                if j==M:
                    return i-M
            else:
                if j != 0:
                    j = LPS[j-1]
                else:
                    ## This line is hard to understand
                    i += 1

        return -1

needle = "aabaaf"
haystack = "aabaabaaf"
sol = Solution()
print(sol.strStr(haystack, needle))