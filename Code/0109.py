class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        record = [0]*26
        for i in s:
            record[ord(i)-ord('a')] += 1
        for i in t:
            record[ord(i)-ord('a')] -= 1
        
        for i in record:
            if i != 0:
                return False
        
        return True


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import defaultdict
        dicA = defaultdict(int)
        dicB = defaultdict(int)

        for i in s:
            dicA[i] += 1
        for i in t:
            dicB[i] += 1
        
        return dicA == dicB

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import Counter
        return Counter(s)==Counter(t)


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        record = [0]*26
        for i in magazine:
            record[ord(i)-ord('a')] += 1
        for i in ransomNote:
            record[ord(i)-ord('a')] -= 1
        
        for i in record:
            if i<0:
                return False
        
        return True

class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        hash = [0]*26
        result = []

        for letter in words[0]:
            hash[ord(letter)-ord('a')] += 1
        
        for str in range(1, len(words)):
            hash_temp = [0]*26
            for letter in words[str]:
                hash_temp[ord(letter)-ord('a')] += 1
            
            for i in range(26):
                hash[i] = min(hash[i], hash_temp[i])
        
        for i in range(26):
            while hash[i]>0:
                result.append(chr(ord('a')+i))
                hash[i] -= 1
        
        return result
words = ["bella","label","roller"]
sol = Solution()
# print(sol.commonChars(words))


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = {}
        result = []

        for i in nums1:
            dic[i] = 1
        
        for i in nums2:
            if i in dic.keys() and dic[i] == 1:
                result.append(i)
                dic[i] = 0
        return result

nums1 = [1,2,2,1,6]
nums2 = [2,2,3,5,9,6]
sol = Solution()
# print(sol.intersection(nums1, nums2))


class Solution(object):
    def sumDigit(self, n):
        sum = 0
        while n:
            sum += (n%10)**2
            n = n//10
        return sum

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dic = {}
        while True:
            sum = self.sumDigit(n)
            if sum==1:
                return True
            elif sum in dic.keys() and dic[sum]==1:
                return False
            dic[sum] = 1
            n = sum

n = 19
# sol = Solution()
# print(sol.isHappy(n))

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}

        for i, num in enumerate(nums):
            if target-num in dic:
                return [i, dic[target-num]]
            else:
                dic[num] = i
        return False

nums = [3, 2, 4]
target = 6
sol = Solution()
print(sol.twoSum(nums, target))


class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        result = 0
        dic = {}

        for i in nums1:
            for j in nums2:
                if (i+j) in dic.keys():
                    dic[i+j] += 1
                else:
                    dic[i+j] = 1

        for i in nums3:
            for j in nums4:
                if -(i+j) in dic.keys():
                    result += dic[-(i+j)]

        return result
    
nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]
sol = Solution()
print(sol.fourSumCount(nums1, nums2, nums3, nums4))