class Solution(object):
    def minimumCardPickup(self, cards):
        distDict = {}
        for i in range(len(cards)):
            card = cards[i]
            if card in distDict:
                last, dist_i = distDict[card]
                distDict[card] = (i, min(dist_i, i - last))
            else:
                distDict[card] = (i, 10000000)
        answer = min(list(map(lambda x: x[1], distDict.values())))
        if answer == 1000000:
            return -1
        return answer + 1

sol = Solution()
cards = list(map(int, input().split()))
print(sol.minimumCardPickup(cards))