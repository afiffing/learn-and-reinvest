# Author Ashish Singh
# sorted vs lambda
# overlap is end[i] < start[j], that means no overlap and append

class solution:
    def __init__(self):
        self.nums = []

    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        self.nums = [intervals[0]]
        print(self.nums[-1][1])
        for interval in intervals:
            if self.nums[-1][1] < interval[0]:
                self.nums.append(interval)
            else:
                self.nums[-1][1] = max(self.nums[-1][1],interval[1])

        return self.nums



if __name__ == "__main__":
    #intervals = [[2,6],[1,3],[15,18],[8,10]]
    #intervals = [[1,4],[4,5]]
    #intervals = [[1,4],[0,4]]
    intervals = [[1, 4], [2, 3]]
    s = solution()
    print(s.merge(intervals))

