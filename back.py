class Event:
    name = 0
    time = 0
    predecessors = []
    es = 0
    ef = 0
    ls = 0
    lf = 0
    slack = 0
    critical = False

    def __init__(self, name, time, predecessors):
        self.name = name
        self.time = time
        self.predecessors = predecessors

eventTable = []

#funkcja liczaca es/ef/ls/lf/slack
#sciezka krytyczna
#tr



