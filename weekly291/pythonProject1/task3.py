HASH_BASE = 2

class Solution(object):
    def subarrayHash(self, subarray, prime):
        hashSum = 0
        power = 1
        for x in subarray[::-1]:
            hashSum += x * power
            hashSum %= prime
            power *= HASH_BASE
        return hashSum

    def fastPower(self, number, power, mod):
        if power == 0:
            return 1
        if power == 1:
            return number % mod
        if power % 2 == 1:
            return (self.fastPower(number, power - 1, mod) * number) % mod
        return self.fastPower(number, power // 2, mod) ** 2 % mod

    def endMoveHash(self, oldHash, oldLength, newElem, mod):
        return (oldHash * HASH_BASE + newElem) % mod

    def beginMoveHash(self, oldHash, oldLength, firstElem, mod):
        power = self.fastPower(nember=HASH_BASE, power=oldLength, mod=mod)
        return (oldHash - firstElem * power + mod) % mod

    def findDevided(self, nums, p):
        devided = []
        for i in range(len(nums)):
            if nums[i] % p == 0:
                devided.append(i)
        return devided

    def countDistinct(self, nums, k, p):
        devided = self.findDevided(nums, p)
        subarraysHashes = {}
        lastDevidedIndex = -1
        # if len(devided) == 0:
        #     devidedCounter = 0
        # else:
        #     devidedCounter = int(devided[0] == 0)
        for end in range(1, len(nums)):

        """
        :type nums: List[int]
        :type k: int
        :type p: int
        :rtype: int
        """