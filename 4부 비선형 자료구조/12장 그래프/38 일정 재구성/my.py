import collections


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        
        a = collections.defaultdict(list)

        print(tickets[0][0])

        for i in len(tickets):
            a[tickets[i][0]].append(tickets[i][1])

        print(a)

        return []


tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
test = Solution()
test.findItinerary(tickets)