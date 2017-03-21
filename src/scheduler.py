import datetime
import dateutil.parser # Hacky format guesser, returning datetime objects

"""
Returns intervals in the units of timeLeft, starting from 0, right now.
"""
def intervals (timeLeft, sessions):
    intervals = []
    for i in range(sessions):
        intervals.append(timeLeft * (1-1/i))
    return intervals

def humanIntervals (intervals):
    hIntervals = []
    for i in intervals:
        hIntervals.append(datetime.datetime.fromutctimestamp(datetime.datetime.now().total_seconds() + i))
    return hIntervals

def humanTime (timeString, sessions = 5):
    return hIntervals(intervals((dateutil.parser(timeString) - datetime.datetime.now()).total_seconds(), sessions))

def main(argv):
    print(humanTime("2017 March 29 23:59"))
    print(humanTime(argv[1]))

if __name__ == "__main__":
    main(sys.argv)
