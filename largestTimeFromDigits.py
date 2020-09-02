def largestTimeFromDigits(self, A):
    return max(("%d%d:%d%d" % time for time in itertools.permutations(A) if time[:2] < (2, 4) and time[2] < 6), default="")
