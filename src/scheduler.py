import datetime
import dateutil.parser # Hacky format guesser, returning datetime objects
import sys

"""
Returns intervals in the units of timeLeft, starting from 0, right now.
"""
def intervals (timeLeft, sessions):
    intervals = []
    for i in range(1,sessions+1):
        intervals.append(timeLeft * (1-1/i))
    return intervals

def humanIntervals (intervals):
    hIntervals = []
    for i in intervals:
        hIntervals.append((datetime.datetime.fromtimestamp(datetime.datetime.now().timestamp() + i)).isoformat())
    return hIntervals

def humanTime (timeString, sessions = 5):
    targetTime = dateutil.parser.parse(timeString) - datetime.datetime.now()
    return humanIntervals(intervals(targetTime.total_seconds(), sessions))

def main(argv):
    print(humanTime("2017 March 29 23:59"))
    print(humanTime(argv[1], int(argv[2])))

if __name__ == "__main__":
    main(sys.argv)
