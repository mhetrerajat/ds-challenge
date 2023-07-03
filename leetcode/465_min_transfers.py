"""
# https://leetcode.com/problems/optimal-account-balancing/
# 465. Optimal Account Balancing
# Weekly Premium - July - W1


You are given an array of transactions transactions where transactions[i] = [fromi, toi, amounti] indicates that the person with ID = fromi gave amounti $ to the person with ID = toi.
Return the minimum number of transactions required to settle the debt. 

Input: transactions = [[0,1,10],[2,0,5]]
Output: 2
Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.
Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.

Input: transactions = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]
Output: 1
Explanation:
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.
Therefore, person #1 only need to give person #0 $4, and all debt is settled.

# Constraints
1 <= transactions.length <= 8
transactions[i].length == 3
0 <= fromi, toi < 12
fromi != toi
1 <= amounti <= 100
"""

from typing import List
from collections import defaultdict


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        # Peron ID may not be linear
        debts = defaultdict(int)

        for f, t, amount in transactions:
            debts[f] -= amount
            debts[t] += amount

        # people with debt
        debt_people = [d for (id, d) in debts.items() if d != 0]

        n = len(debt_people)

        # backtrack
        # start with 0 idx, and settle
        # at index, pidx, all person before pidx are settled
        def backtrack(pidx):
            while pidx < n and debt_people[pidx] == 0:
                pidx += 1

            if pidx == n:
                return 0

            answer = float("inf")
            for i in range(pidx + 1, n):
                # find person which don't have any debt i.e. val is -ve
                if debt_people[pidx] * debt_people[i] < 0:
                    debt_people[i] += debt_people[pidx]
                    answer = min(answer, backtrack(pidx + 1) + 1)
                    debt_people[i] -= debt_people[pidx]
            return answer

        return backtrack(0)


testcases = [
    ([[0, 1, 10], [2, 0, 5]], 2),
    ([[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]], 1),
]
for transactions, expected in testcases:
    s = Solution()
    assert s.minTransfers(transactions) == expected
