class Solution(object):

    def getNumberWithoutIndex(self, number, index):
        strRepr = str(number)
        return int(strRepr[:index] + strRepr[index + 1:])

    def removeDigit(self, number, digit):
        pass

sol = Solution(None)
print(sol.getNumberWithoutIndex(12345, 3))