import time
from collections import deque
from Solver import Solver

goalTest = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


class BFS(Solver):

    def solve(self):
        self.expandedNodes += 1
        before = time.process_time()
        frontier = deque([self.initialState])
        self.explored.add(self.initialState.tilesOrder)
        print('*')
        print(self.initialState.tilesOrder)
        while frontier:
            state = frontier.popleft()
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
