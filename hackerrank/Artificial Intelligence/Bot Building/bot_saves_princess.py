#!/bin/python

def displayPathToPrincess(N, grid):
    m_x, m_y = 0,0
    p_x, p_y = 0,0

    for x in xrange(N):
        for y in xrange(len(grid[x])):
            if grid[x][y] == 'm':
                m_x = x
                m_y = y
            elif grid[x][y] == 'p':
                p_x = x
                p_y = y

    output = []


    delta_x = p_x - m_x
    delta_y = p_y - m_y
    while delta_x == 0 && delta_y == 0:
        if delta_x < 0:
            output.append("UP")
        elif delta_x > 0:
            output.append("DOWN")

        if delta_y < 0:
            output.append("LEFT")
        elif delta_y > 0:
            output.append("RIGHT")

    return output


if __name__ == "__main__":
    N = int(input())
    grid = []
    for item in xrange(0,N):
        grid.append(raw_input().strip())

    print displayPathToPrincess(N, grid)
