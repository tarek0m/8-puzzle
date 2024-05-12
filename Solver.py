class Solver:

    def __init__(self, initialState):
        self.initialState = initialState
        self.explored = set()
        self.depth = 0
        self.expandedNodes = 0
