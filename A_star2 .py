# -----------
# User Instructions:
# 
# Modify the function search so that it returns
# a table of values called expand. This table
# will keep track of which step each node was
# expanded.
#
# Make sure that the initial cell in the grid 
# you return has the value 0.
# ----------

grid = [[0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

action = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]

heuristic= [[9,8,7,6,5,4],
			[8,7,6,5,4,3],
			[7,6,5,4,3,2],
			[6,5,4,3,2,1],
			[5,4,3,2,1,0]]

closed2 = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]

expand = closed2
for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j]==1:
				expand[i][j] = -1			

def search(grid,init,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1
    global expand
	

    x = init[0]
    y = init[1]
    g = 0
    h = heuristic[x][y]
    f = g + h

    open = [[f, g, h, x, y]]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand
    step = 0
    while not found and not resign:
        if len(open) == 0:
            resign = True
            print 'fail'
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[3]
            y = next[4]
            g = next[1]
            expand[x][y] = step
            step = step+1
            
            if x == goal[0] and y == goal[1]:
                found = True
                print next
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g  + cost
                            f2 = g2 + heuristic[x2][y2]
                            open.append([f2, g2,heuristic[x2][y2], x2, y2])
                            closed[x2][y2] = 1
                            action[x2][y2] = i

search(grid,init,goal,cost)
print action

policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
x = goal[0]
y = goal[1]
policy[x][y] = '*'



while x!=init[0] or y!=init[1]:
	x2 = x - delta[action[x][y]][0]
	y2 = y - delta[action[x][y]][1]
	policy[x2][y2] = delta_name[action[x][y]]
	x=x2
	y=y2
	 
for i in range(len(grid)):
	print expand[i]
