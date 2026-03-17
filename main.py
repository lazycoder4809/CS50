class Node:
        def __init__(self, state, parent, action):
            self.state = state
            self.parent = parent
            self.action = action


class StackFrontier:
        def __init__(self):
            self.frontier = []

        def add_node(self, node):
            self.frontier.append(node)

        def contains_state(self, state):
            return any(node.state == state for node in self.frontier)

        def empty(self):
            return len(self.frontier) == 0

        def remove_node(self):
            if self.empty():
                raise Exception("empty frontier")
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):
        def remove_node(self):
            if self.empty():
                raise Exception("empty frontier")
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node



class Maze:
        def __init__(self, filename):
            with open(filename) as f:
                contents = f.read()

            if contents.count("A") != 1:
                raise Exception("Maze must have exactly one start (A)")
            if contents.count("B") != 1:
                raise Exception("Maze must have exactly one goal (B)")

            contents = contents.splitlines()
            self.height = len(contents)
            self.width = max(len(line) for line in contents)

            self.walls = []

            for i in range(self.height):
                row = []

                line = contents[i].ljust(self.width, "#")

                for j in range(self.width):

                    if line[j] == "A":
                        self.start = (i, j)
                        row.append(False)

                    elif line[j] == "B":
                        self.goal = (i, j)
                        row.append(False)

                    elif line[j] == " ":
                        row.append(False)

                    elif line[j] == "#":
                        row.append(True)

                    else:
                        row.append(True)

                self.walls.append(row)


            self.solution = None

        def neighbors(self, state):
            row, col = state

            candidates = [
                ("up", (row - 1, col)),
                ("down", (row + 1, col)),
                ("left", (row, col - 1)),
                ("right", (row, col + 1))
            ]

            result = []
            for action, (r, c) in candidates:
                if 0 <= r < self.height and 0 <= c < self.width:
                    if not self.walls[r][c]:
                        result.append((action, (r, c)))

            return result

        def solve(self):
            self.explored = set()

            start = Node(self.start, None, None)
            frontier = QueueFrontier()   
            frontier.add_node(start)

            while True:

                if frontier.empty():
                    raise Exception("No solution")

                node = frontier.remove_node()

                if node.state == self.goal:

                    actions = []
                    cells = []

                    while node.parent is not None:
                        actions.append(node.action)
                        cells.append(node.state)
                        node = node.parent

                    actions.reverse()
                    cells.reverse()

                    self.solution = (actions, cells)
                    return

                self.explored.add(node.state)

                for action, state in self.neighbors(node.state):
                    if not frontier.contains_state(state) and state not in self.explored:
                        child = Node(state, node, action)
                        frontier.add_node(child)

        def print(self):
            solution = self.solution[1] if self.solution else None
            print(len(self.explored))
            for i, row in enumerate(self.walls):
                for j, col in enumerate(row):
                    if col:
                        print("█", end="")
                    elif (i, j) == self.start:
                        print("A", end="")
                    elif (i, j) == self.goal:
                        print("B", end="")
                    elif solution and (i, j) in solution:
                        print("*", end="")
                    else:
                        print(" ", end="")
                print()

maze_text = """\
    ############################
    #A         #               #
    #  ####### # ######## ###  #
    #  #     # # #      #   #  #
    #  # ### # # # #### # # #  #
    #  # #   # #   #    # # #  #
    #  # # ### ##### #### # #  #
    #  # # #         #    # #  #
    #  #   # ####### # #### #  #
    #  #   # #     # #    # #  #
    #  ##### # ### # #### # #  #
    #        #   # #    #   #  #
    # ############ # # #### #  #
    #              #   #    #  #
    ################## #### #  #
    #                  #    #  #
    # ################ # ## #  #
    # #              # #  # #  #
    # # ############ # ## # #  #
    # # #          # #  # # #  #
    # # # ######## # ## # # #  #
    # # # #      # #  # # # #  # 
    # # # # #### # ## # # # #  #
    # # # # #  # #  # # # # #  #
    # #   # #  # #    # # # #  #
    # ##### #  # ###### # # #  #
    #          #        # # #  #
    # ########## ######## # #  #
    #                     #   B#
    ############################
    """
    

with open("maze.txt", "w") as f:
        f.write(maze_text)


    
maze = Maze("maze.txt")
maze.solve()
maze.print()    