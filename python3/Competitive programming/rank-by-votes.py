# Author: Ashish Singh
# rank by votes are 2 d array with dictionary
# use of enumerate
# use of lambda

class Solution:
    def __init__(self, votes):
        self.d = {}
        self.votes = votes

    def rankTeams(self):
        for vote in votes:  # ABC
            for i, char in enumerate(vote):  # [(0,A), (1,B), (2,C)]
                if char not in self.d:
                    self.d[char] = [0] * len(vote)  # {'A':[0,0,0], ...
                self.d[char][i] += 1
        voted_names = sorted(self.d.keys()) #ABC
        return "".join(sorted(voted_names,key=lambda x:self.d[x], reverse=True ))


if __name__ == "__main__":
    votes = ["ABC", "ACB", "ABC", "ACB", "ACB"]
    sol = Solution(votes)
    print(sol.rankTeams())
