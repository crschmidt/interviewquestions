# initially, I basically said "Well, this is one of those
# graph theory problems that I'm probably not good at."

# I then started to sketch various ways of turning the
# problem into a graph:


nodes = {}

#1 1 0 0
#1 1 0 0   -- would return 2
#0 0 0 1
nodes[(0,0)] = [(1,0), (0,1)]
nodes[(1,0)] = [(1,1), (0,0)]

# but quickly realized this wouldn't work.

# The interviewer tried to point me in the right
# direction by asking questions like "How would you
# not revisit the same nodes/go in loops? How about
# if you can cahnge the values?"

# He then just had me traverse a graph from a given
# node and reset the values:

def reset(node):
    for component in node.components:
        if component.val == 1:
            reset(component)
            component.val = 0

# We ran out of time at this point, but on the way out,
# he pointed out that if you can change the values, you
# can just explore the space and reset the values as you
# do it; while I waited for the next interviewer, I
# used that to write up the solution on the whiteboard

def reset(matrix, x, y):
    if matrix[x][y]:
        matrix[x][y] = 0
        if x+ 1 < len(matrix):
            reset(matrix, x+1, y)
        if y+1 < len(matrix[x]):
            reset(matrix, x, y+1)
        # initially, I thought that since I
        # was always going down and to the right,
        # i could skip these checks, but then I
        # realized that *components* can go down
        # and to the left.
        if y > 0:
            reset(matrix, x, y-1)
        if x> 0:
            reset(matrix, x-1, y)

def con(matrix):
    con = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]:
                con += 1
                reset(matrix, i, j)
    return con

