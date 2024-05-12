import time
from Solver import Solver

goalTest = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


class DFS(Solver):

    def solve(self):
        before = time.process_time()
        frontier = [self.initialState]
        self.explored.add(self.initialState.tilesOrder)
        while frontier:
            self.expandedNodes += 1
            state = frontier.pop()
            state.manhattanFn()
            if state.board == goalTest:
                self.finalState = state
                self.runningTime = time.process_time() - before
                return True
            if state.depth + 1 > self.depth:
                self.depth = state.depth + 1
            for neighbor in state.neighbors():
                if not (neighbor.tilesOrder in self.explored):
                    self.explored.add(neighbor.tilesOrder)
                    print('**')
                    print(neighbor.tilesOrder)
                    frontier.append(neighbor)
        self.runningTime = time.process_time() - before
        return False
