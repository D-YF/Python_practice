import array as arr
class bubbleSort():
    def bubbleSort(array):
        n = len(array)
        swapped = False

        if (array == None) or n < 2:
            return
        
        for i in range(n-1):
            for j in range(n-i-1):
                if array[j]>array[j+1]:
                    swapped = True
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp

            if not swapped:
                break

ar = [2,3,2,5,1,2,6,8,4,7,6,9,4,0,2]
# bubbleSort.bubbleSort(ar)
# print(ar)

def printOddTimesNum1(arr):
    eor = 0
    for a in arr:
        eor = eor ^ a
    print(eor)
arr_odd = [1,1,2,2,3,3,4,5,5]
# printOddTimesNum1(arr_odd)

def printOddTimesNum2(arr):
    eor = 0
    for a in arr:
        eor = eor ^ a
    rightOne = (~eor+1) & eor 
    onlyone = 0
    for a in arr:
        if (a & rightOne) == 0 :
        # if (a & rightOne)  : # both okay
            onlyone = onlyone ^ a
    
    print(onlyone)
    print(onlyone ^ eor)

arr_odd2 = [1,1,2,2,2,3,3,4,5,5]
# printOddTimesNum2(arr_odd2)

class InsertionSort():
    def InsertionSort(arr):
        n = len(arr)
        if (arr == None) or (n < 2):
            return
        
        for i in range(1, n):
            j = i-1
            while j>=0 and arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                j -= 1
    
ar = [1,3,2,5,1,2,6,8,4,7,6,9,4,0,2]
# InsertionSort.InsertionSort(ar)
# print(ar)


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        record = dict()
        for idx,num in enumerate(nums):
            if target-num not in record:
                record[num] = idx
            else:
                return [record[target-num], idx]

nums = [2, 7, 11,15]
target = 9
Sol = Solution()
s = Sol.twoSum(nums=nums, target=target)
print(s)

                
