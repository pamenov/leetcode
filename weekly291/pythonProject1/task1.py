class Solution(object):

    def getNumberWithoutIndex(self, number, index):
        strRepr = str(number)
        if index == -1:
            return number
        return strRepr[:index] + strRepr[index + 1:]

    def removeDigit(self, number, digit):
        stringToSearch = str(number)
        strDigit = str(digit)
        index = stringToSearch.find(strDigit)
        maxNumber = 0
        while True:
            newNumber = self.getNumberWithoutIndex(number, index)
            print(newNumber, index)
            maxNumber = max(maxNumber, newNumber)
            stringToSearch = stringToSearch[index + 1:]
            incIndex = stringToSearch.find(strDigit)
            if incIndex == -1:
                break
            index += incIndex
        return maxNumber

# class Solution(object):
#     def getNumberWithoutIndex(self, number, index):
#         strRepr = str(number)
#         if index == -1:
#             return number
#         return strRepr[:index] + strRepr[index + 1:]
#
#     def removeDigit(self, number, digit):
#         strDigit = str(digit)
#         strNumber = str(number)
#         ans = '0'
#         for i in range(len(strNumber)):
#             if strNumber[i] == strDigit:
#                 if i == len(strNumber) - 1:
#                     return strNumber[: -1]
#                 if strNumber[i + 1] > strNumber[i]:
#                     return self.getNumberWithoutIndex(number, i)
#                 if strNumber[i + 1] < strNumber[i]:
#                     ans = self.getNumberWithoutIndex(number, i)
#         return ans


sol = Solution()
# print(sol.getNumberWithoutIndex(12345, 0))
number = int(input())
digit = int(input())
print(sol.removeDigit(number, digit))