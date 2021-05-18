"""
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

"""


# Space hungry
# nlogn
def trivial(N):
    events = []

    for (start, end) in N:
        events.append((start, 'start'))
        events.append((end, 'end'))

    events.sort()
    
    _max = 0
    current = 0

    for (v, _type) in events:
        if _type == "start":
            current += 1
        elif _type == "end":
            current -= 1

        if _max < current:
            _max = current

    return _max

def better(N):
    start, end = map(list, zip(*N))

    start.sort()
    end.sort()

    _max = 0
    current = 0
    sdx = 0
    edx = 0
    length = len(start)

    while sdx < length and edx < length:
        if start[sdx] <= end[edx]:
            current += 1
            sdx += 1
        else:
            current -= 1
            edx += 1

        if _max < current:
            _max = current

    return _max

def get_room_count(N):
    return better(N)

if __name__ == "__main__":
    N = [
        (30, 75),
        (0, 50),
        (60, 150)
    ]
    assert get_room_count(N) == 2
